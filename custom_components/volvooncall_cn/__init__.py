from datetime import timedelta
import logging
import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import callback
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .volvooncall_cn import VehicleAPI
from .volvooncall_cn import Vehicle
from .volvooncall_cn import DOMAIN

PLATFORMS = {
    "sensor": "sensor",
    "binary_sensor": "binary_sensor",
    "device_tracker": "device_tracker",
    "lock": "lock",
    "button": "button",
    "number": "number",
    "switch": "switch",
}

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry):
    """Config entry example."""
    session = async_get_clientsession(hass)

    volvo_api = VehicleAPI(session=session, username=entry.data["username"], password=entry.data["password"])
    hass.data.setdefault(DOMAIN, {})
    coordinator = hass.data[DOMAIN][entry.entry_id] = VolvoCoordinator(hass, volvo_api)

    # Fetch initial data so we have data when entities subscribe
    #
    # If the refresh fails, async_config_entry_first_refresh will
    # raise ConfigEntryNotReady and setup will try again later
    #
    # If you do not want to retry setup on failure, use
    # coordinator.async_refresh() instead
    #
    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


class VolvoCoordinator(DataUpdateCoordinator):
    """My custom coordinator."""

    def __init__(self, hass, volvo_api):
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name="Volvo On Call CN sensor",
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=30),
        )
        self.volvo_api = volvo_api

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            # Note: asyncio.TimeoutError and aiohttp.ClientError are already
            # handled by the data update coordinator.
            async with async_timeout.timeout(30):
                # Grab active context variables to limit data required to be fetched from API
                # Note: using context is not required if there is no need or ability to limit
                # data retrieved from API.
                await self.volvo_api.login()
                await self.volvo_api.update_token()
                vinVehicleMaps = await self.volvo_api.get_vehicles_vins()
                vehicles = []
                for vin, vehicleInfos in vinVehicleMaps.items():
                    modelYear = int(vehicleInfos.get("modelYear", 2020))
                    isAaos = modelYear >= 2022
                    vehicle = Vehicle(vin, self.volvo_api, isAaos)
                    await vehicle.update()
                    vehicles.append(vehicle)

                return vehicles
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")


metaMap = {
    "car_lock": {
        "name": "Lock",
        "device_class": None,
        "icon": "",
        "unit": "",
    },
    # "car_lock_open": {
    #    "name": "Lock",
    #    "device_class": "lock",
    #    "icon": "",
    #    "unit": "",
    # },
    "window_lock": {
        "name": "Winodw Lock",
        "device_class": None,
        "icon": "",
        "unit": "",
    },
    # "remote_door_unlock": {
    #    "name": "Remote Door Unlock",
    #    "device_class": "lock",
    #    "icon": "",
    #    "unit": "",
    # },
    "distance_to_empty": {
        "name": "Distance to empty",
        "device_class": None,
        "icon": "mdi:ruler",
        "unit": "km",
    },
    "tail_gate_open": {
        "name": "Tail gate",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "rear_right_door_open": {
        "name": "Rear right door",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "rear_left_door_open": {
        "name": "Rear left door",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "front_right_door_open": {
        "name": "Front right door",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "front_left_door_open": {
        "name": "Front left door",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "hood_open": {
        "name": "Hood",
        "device_class": "door",
        "icon": "",
        "unit": "",
    },
    "sunroof_open": {
        "name": "Sunroof",
        "device_class": "window",
        "icon": "",
        "unit": "",
    },
    "engine_running": {
        "name": "Engine",
        "device_class": "power",
        "icon": "",
        "unit": "",
    },
    "odo_meter": {
        "name": "Odometer",
        "device_class": None,
        "icon": "mdi:speedometer",
        "unit": "km",
    },
    "front_left_window_open": {
        "name": "Front left window",
        "device_class": "window",
        "icon": "",
        "unit": "",
    },
    "front_right_window_open": {
        "name": "Front right window",
        "device_class": "window",
        "icon": "",
        "unit": "",
    },
    "rear_left_window_open": {
        "name": "Rear left window",
        "device_class": "window",
        "icon": "",
        "unit": "",
    },
    "rear_right_window_open": {
        "name": "Rear right window",
        "device_class": "window",
        "icon": "",
        "unit": "",
    },
    "fuel_amount": {
        "name": "Fuel amount",
        "device_class": "VOLUME_STORAGE",
        "icon": "mdi:gas-station",
        "unit": "L",
    },
    # TODO
    # "fuel_amount_level": {
    #    "name": "Fuel amount level",
    #    "device_class": None,
    #    "icon": "mdi:gas-station",
    #    "unit": "%",
    # },
    "position": {
        "name": "Position",
        "device_class": None,
        "icon": "",
        "unit": "",
    },
    "position_wgs84": {
        "name": "Position WGS84",
        "device_class": None,
        "icon": "",
        "unit": "",
    },
    "flash_button": {
        "name": "Flash",
        "device_class": None,
        "icon": "mdi:car-light-high",
        "unit": "",
    },
    "honk_flash_button": {
        "name": "Honk And Flash",
        "device_class": None,
        "icon": "mdi:bugle",
        "unit": "",
    },
    "engine_duration_number": {
        "name": "Engine Duration",
        "device_class": None,
        "icon": "mdi:clock-time-eight-outline",
        "unit": "Minute",
    },
    "engine_switch": {
        "name": "Engine Remote control",
        "device_class": None,
        "icon": "mdi:engine-outline",
        "unit": "",
    }
}


class VolvoEntity(CoordinatorEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, context=idx)
        self.idx = idx
        self.metaMapKey = metaMapKey

    @property
    def name(self):
        return f"{self.coordinator.data[self.idx].vin} {metaMap[self.metaMapKey]['name']}"

    @property
    def icon(self):
        return metaMap[self.metaMapKey]["icon"]

    @property
    def device_class(self):
        return metaMap[self.metaMapKey]["device_class"]

    @property
    def device_info(self) -> DeviceInfo:
        """Return a inique set of attributes for each vehicle."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.data[self.idx].vin)},
            name="Volvo " + self.coordinator.data[self.idx].series_name,
            model=self.coordinator.data[self.idx].series_name + " " + self.coordinator.data[self.idx].model_name,
            manufacturer="Volvo",
        )

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self.coordinator.data[self.idx].vin}-{self.metaMapKey}"
