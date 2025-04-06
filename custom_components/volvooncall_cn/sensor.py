from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import Platform

from . import VolvoCoordinator, VolvoEntity, metaMap
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
    for idx, _ in enumerate(coordinator.data):
        entities.append(VolvoSensor(coordinator, idx, "distance_to_empty"))
        entities.append(VolvoSensor(coordinator, idx, "odo_meter"))
        entities.append(VolvoSensor(coordinator, idx, "fuel_amount"))
        entities.append(VolvoSensor(coordinator, idx, "fuel_average_consumption_liters_per_100_km"))
        entities.append(VolvoSensor(coordinator, idx, "service_warning_msg"))
        # entities.append(VolvoSensor(coordinator, idx, "fuel_amount_level"))

    async_add_entities(entities)


class VolvoSensor(VolvoEntity, SensorEntity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available
    """

    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, idx, metaMapKey, Platform.SENSOR)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data[self.idx].get(self.metaMapKey)
        self._attr_native_unit_of_measurement = metaMap[self.metaMapKey]["unit"]
        self.async_write_ha_state()
