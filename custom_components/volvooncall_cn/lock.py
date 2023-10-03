from __future__ import annotations
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

from . import VolvoCoordinator, VolvoEntity
from . import metaMap

DOMAIN = "volvooncall_cn"

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
        return self.coordinator.data[self.idx].toMap()["car_locked"]

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the car."""
        await self.coordinator.data[self.idx].lock()
        await self.coordinator.async_request_refresh()

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the car."""
        await self.coordinator.data[self.idx].unlock()
        await self.coordinator.async_request_refresh()
