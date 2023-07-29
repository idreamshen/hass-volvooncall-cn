from __future__ import annotations

from homeassistant.components.device_tracker.config_entry import TrackerEntity
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
        entities.append(VolvoSensor(coordinator, idx, "position"))

    async_add_entities(entities)

class VolvoSensor(VolvoEntity, TrackerEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def source_type(self)
        """Handle updated data from the coordinator."""
        return "gps"

    @property
    def latitude(self)
        """Handle updated data from the coordinator."""
        return self.coordinator.data[self.idx].toMap()[self.metaMapKey]["latitude"]

    @property
    def longitude(self)
        """Handle updated data from the coordinator."""
        return self.coordinator.data[self.idx].toMap()[self.metaMapKey]["longitude"]
