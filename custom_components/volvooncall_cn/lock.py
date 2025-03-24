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
from .volvooncall_base import MAX_RETRIES

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
        if ent.get("isAaos"):
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

    async def _update_status(self, is_locked):
        for _ in range(MAX_RETRIES):
            await asyncio.sleep(1)
            await self.coordinator.async_refresh()
            if self.is_locked == is_locked:
                break

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the car."""
        await self.coordinator.data[self.idx].lock_vehicle()
        await self._update_status(True)

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the car."""
        await self.coordinator.data[self.idx].unlock_vehicle()
        await self._update_status(False)


class VolvoWindowSensor(VolvoEntity, LockEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def is_locked(self) -> bool:
        data = self.coordinator.data[self.idx]
        window_keys = ["front_left_window_open", "front_right_window_open",
                       "rear_right_window_open", "rear_left_window_open"]
        for window in window_keys:
            is_open = data.get(window)
            _LOGGER.debug("%s %s", window, is_open)
            if is_open:
                return False
        return True

    async def _update_status(self, is_locked):
        for _ in range(MAX_RETRIES):
            __ = await asyncio.sleep(5)
            __ = await self.coordinator.async_refresh()
            if self.is_locked == is_locked:
                break

    async def async_lock(self, **kwargs: Any) -> None:
        await self.coordinator.data[self.idx].lock_window()
        await self._update_status(True)

    async def async_unlock(self, **kwargs: Any) -> None:
        await self.coordinator.data[self.idx].unlock_window()
        await self._update_status(False)
