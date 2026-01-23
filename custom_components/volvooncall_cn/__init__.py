from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
import asyncio
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_SCAN_INTERVAL, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN
from .store import VolvoStore
from aiohttp import ClientError

from .volvooncall_base import DEFAULT_SCAN_INTERVAL, VolvoAPIError
from .volvooncall_cn import Vehicle, VehicleAPI

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
    Platform.LOCK,
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SWITCH,
]


@dataclass
class VolvoRuntimeData:
    coordinator: "VolvoCoordinator"
    api: VehicleAPI


async def _async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    if entry.version == 1:
        data = dict(entry.data)
        options = dict(entry.options)
        if CONF_SCAN_INTERVAL in data and CONF_SCAN_INTERVAL not in options:
            options[CONF_SCAN_INTERVAL] = data.pop(CONF_SCAN_INTERVAL)
        hass.config_entries.async_update_entry(entry, data=data, options=options, version=2)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    session = async_get_clientsession(hass)
    if CONF_SCAN_INTERVAL in entry.data and CONF_SCAN_INTERVAL not in entry.options:
        data = dict(entry.data)
        options = dict(entry.options)
        options[CONF_SCAN_INTERVAL] = data.pop(CONF_SCAN_INTERVAL)
        hass.config_entries.async_update_entry(entry, data=data, options=options)

    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)
    interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    volvo_api = VehicleAPI(session=session, username=username, password=password)
    coordinator = VolvoCoordinator(hass, volvo_api, interval)
    entry.runtime_data = VolvoRuntimeData(coordinator=coordinator, api=volvo_api)

    entry.async_on_unload(entry.add_update_listener(_async_update_options))
    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        entry.runtime_data = None
    return unload_ok


class VolvoCoordinator(DataUpdateCoordinator[list[Vehicle]]):
    def __init__(self, hass: HomeAssistant, volvo_api: VehicleAPI, scan_interval: int) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name="Volvo On Call CN",
            update_interval=timedelta(seconds=scan_interval),
            always_update=False,
        )
        self.volvo_api = volvo_api
        self._vehicles: dict[str, Vehicle] = {}
        self.stores: dict[str, VolvoStore] = {}

    async def _async_setup(self) -> None:
        await self.volvo_api.login()

    async def _async_update_data(self) -> list[Vehicle]:
        try:
            async with asyncio.timeout(30):
                await self.volvo_api.login()
                await self.volvo_api.update_token()
                vin_vehicle_map = await self.volvo_api.get_vehicles_vins()
                current_vins = set(vin_vehicle_map)

                for vin in list(self._vehicles):
                    if vin not in current_vins:
                        self._vehicles.pop(vin)
                        self.stores.pop(vin, None)

                for vin, vehicle_info in vin_vehicle_map.items():
                    if vin not in self._vehicles:
                        model_year = int(vehicle_info.get("modelYear", 2020))
                        is_aaos = model_year >= 2022
                        self._vehicles[vin] = Vehicle(vin, self.volvo_api, is_aaos)
                    if vin not in self.stores:
                        store = VolvoStore(self.hass, vin)
                        await store.load_create_data()
                        self.stores[vin] = store

                await asyncio.gather(
                    *(vehicle.update() for vehicle in self._vehicles.values())
                )

                return list(self._vehicles.values())
        except VolvoAPIError as err:
            raise ConfigEntryAuthFailed(str(err)) from err
        except TimeoutError as err:
            raise UpdateFailed(f"Timeout communicating with API: {err}") from err
        except ClientError as err:
            raise UpdateFailed(f"Network error communicating with API: {err}") from err
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err


class VolvoEntity(CoordinatorEntity[VolvoCoordinator]):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: EntityDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._vehicle = vehicle
        self._attr_unique_id = f"{vehicle.vin}-{description.key}"
        self._attr_translation_key = description.translation_key or description.key

    @property
    def vehicle(self) -> Vehicle:
        # Fetch the latest vehicle reference from coordinator to avoid stale data
        for v in self.coordinator.data:
            if v.vin == self._vehicle.vin:
                return v
        # Fallback to stored reference if not found (shouldn't happen normally)
        return self._vehicle

    @property
    def device_info(self) -> DeviceInfo:
        series_name = self._vehicle.series_name or self._vehicle.model_name or self._vehicle.vin
        model_name = f"{self._vehicle.series_name} {self._vehicle.model_name}".strip()
        return DeviceInfo(
            identifiers={(DOMAIN, self._vehicle.vin)},
            name=f"Volvo {series_name}",
            model=model_name,
            manufacturer="Volvo",
        )

    @property
    def translation_placeholders(self) -> dict[str, str]:
        nickname = self._vehicle.nickname or self._vehicle.series_name or self._vehicle.model_name
        return {"nickname": nickname or self._vehicle.vin}
