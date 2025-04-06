from __future__ import annotations
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import Platform

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure sensors from a config entry created in the integrations UI."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = []
    for idx, ent in enumerate(coordinator.data):
        # entities.append(VolvoSensor(coordinator, idx, "car_lock_open"))
        # entities.append(VolvoSensor(coordinator, idx, "remote_door_unlock"))
        entities.append(VolvoSensor(coordinator, idx, "tail_gate_open"))
        entities.append(VolvoSensor(coordinator, idx, "rear_right_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "rear_left_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "front_right_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "front_left_door_open"))
        entities.append(VolvoSensor(coordinator, idx, "hood_open"))
        entities.append(VolvoSensor(coordinator, idx, "engine_running"))
        entities.append(VolvoWindowSensor(coordinator, idx, "front_left_window_open"))
        entities.append(VolvoWindowSensor(coordinator, idx, "front_right_window_open"))
        entities.append(VolvoWindowSensor(coordinator, idx, "rear_left_window_open"))
        entities.append(VolvoWindowSensor(coordinator, idx, "rear_right_window_open"))
        entities.append(VolvoSensor(coordinator, idx, "sunroof_open"))
        entities.append(VolvoSensor(coordinator, idx, "service_warning"))
        entities.append(VolvoSensor(coordinator, idx, "brake_fluid_level_warning"))
        entities.append(VolvoSensor(coordinator, idx, "engine_coolant_level_warning"))
        entities.append(VolvoSensor(coordinator, idx, "oil_level_warning"))
        entities.append(VolvoSensor(coordinator, idx, "washer_fluid_level_warning"))
        entities.append(VolvoSensor(coordinator, idx, "front_left_tyre_pressure_warning"))
        entities.append(VolvoSensor(coordinator, idx, "front_right_tyre_pressure_warning"))
        entities.append(VolvoSensor(coordinator, idx, "rear_left_tyre_pressure_warning"))
        entities.append(VolvoSensor(coordinator, idx, "rear_right_tyre_pressure_warning"))

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
        super().__init__(coordinator, idx, metaMapKey, Platform.BINARY_SENSOR)

    @property
    def is_on(self) -> bool | None:
        """Handle updated data from the coordinator."""
        return self.coordinator.data[self.idx].get(self.metaMapKey)


class VolvoWindowSensor(VolvoSensor):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def extra_state_attributes(self):
        metaKey = self.metaMapKey + "_ajar"
        return {"open_status_ajar": self.coordinator.data[self.idx].get(metaKey)}
