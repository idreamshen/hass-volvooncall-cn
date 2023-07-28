from __future__ import annotations
from homeassistant.components.binary_sensor import (
    DEVICE_CLASSES_SCHEMA,
    BinarySensorEntity,
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

from . import MyCoordinator, VolvoEntity
from . import metaMap

DOMAIN = "volvooncall_cn"

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure sensors from a config entry created in the integrations UI."""
    coordinator: MyCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = []
    for idx, ent in enumerate(coordinator.data):
        entities.append(VolvoSensor(coordinator, idx, "car_lock_open"))
        entities.append(VolvoSensor(coordinator, idx, "tail_gate_open"))
        entities.append(VolvoSensor(coordinator, idx, "rear_right_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "rear_left_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "front_right_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "front_left_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "hood_open"))
        entities.append(VolvoSensor(coordinator, idx, "engine_running"))

    async_add_entities(entities)

class VolvoSensor(VolvoEntity, BinarySensorEntity):
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
    def is_on(self) -> bool | None:
        """Handle updated data from the coordinator."""
        return self.coordinator.data[self.idx].toMap()[self.metaMapKey]
