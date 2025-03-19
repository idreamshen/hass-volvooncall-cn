from __future__ import annotations
import asyncio
from homeassistant.components.lock import (
    LockEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
import logging

from . import VolvoCoordinator, VolvoEntity
from . import metaMap
from .volvooncall_cn import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure sensors from a config entry created in the integrations UI."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = []
    for idx, ent in enumerate(coordinator.data):
        entities.append(VolvoSensor(coordinator, idx, "car_lock"))
        entities.append(VolvoWindowSensor(coordinator, idx, "window_lock"))

    async_add_entities(entities)


class VolvoSensor(VolvoEntity, LockEntity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available
    """

    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def is_locked(self) -> bool | None:
        """Handle updated data from the coordinator."""
        return self.coordinator.data[self.idx].get("car_locked")

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the car."""
        data = self.coordinator.data[self.idx]
        if data.get("engine_running"):
            raise Exception("Engine running!  Prohibited to lock the car")
        await self.coordinator.data[self.idx].lock_vehicle()
        await self.coordinator.async_request_refresh()

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the car."""
        data = self.coordinator.data[self.idx]
        if data.get("engine_running"):
            raise Exception("Engine running!  Prohibited to unlock the car")
        await self.coordinator.data[self.idx].unlock_vehicle()
        await self.coordinator.async_request_refresh()


class VolvoWindowSensor(VolvoEntity, LockEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def is_locked(self) -> bool | None:
        data = self.coordinator.data[self.idx]
        window_keys = ["front_left_window_open", "front_right_window_open",
                       "rear_right_window_open", "rear_left_window_open"]
        for window in window_keys:
            is_open = data.get(window)
            _LOGGER.debug("%s %s", window, is_open)
            if is_open:
                return False
        return True

    async def async_lock(self, **kwargs: Any) -> None:
        data = self.coordinator.data[self.idx]
        if data.get("engine_running"):
            raise Exception("Engine running!  Prohibited to lock windows")
        await self.coordinator.data[self.idx].lock_window()
        await asyncio.sleep(2)
        await self.coordinator.async_request_refresh()

    async def async_unlock(self, **kwargs: Any) -> None:
        data = self.coordinator.data[self.idx]
        if data.get("engine_running"):
            raise Exception("Engine running!  Prohibited to unlock windows")
        await self.coordinator.data[self.idx].unlock_window()
        await asyncio.sleep(2)
        await self.coordinator.async_request_refresh()
