from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Vehicle], bool | None]
    extra_attributes_fn: Callable[[Vehicle], Mapping[str, bool] | None] | None = None


DIAGNOSTIC_PROBLEM = VolvoBinarySensorEntityDescription(
    key="service_warning",
    device_class=BinarySensorDeviceClass.PROBLEM,
    entity_category=EntityCategory.DIAGNOSTIC,
    entity_registry_enabled_default=False,
    value_fn=lambda vehicle: vehicle.service_warning,
)

WARNING_DESCRIPTIONS: tuple[VolvoBinarySensorEntityDescription, ...] = (
    VolvoBinarySensorEntityDescription(
        key="brake_fluid_level_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.brake_fluid_level_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="engine_coolant_level_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.engine_coolant_level_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="oil_level_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.oil_level_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="washer_fluid_level_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.washer_fluid_level_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="front_left_tyre_pressure_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.front_left_tyre_pressure_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="front_right_tyre_pressure_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.front_right_tyre_pressure_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_left_tyre_pressure_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.rear_left_tyre_pressure_warning,
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_right_tyre_pressure_warning",
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: vehicle.rear_right_tyre_pressure_warning,
    ),
)


BINARY_SENSOR_DESCRIPTIONS: tuple[VolvoBinarySensorEntityDescription, ...] = (
    VolvoBinarySensorEntityDescription(
        key="tail_gate_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.tail_gate_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_right_door_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.rear_right_door_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_left_door_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.rear_left_door_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="front_right_door_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.front_right_door_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="front_left_door_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.front_left_door_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="hood_open",
        device_class=BinarySensorDeviceClass.DOOR,
        value_fn=lambda vehicle: vehicle.hood_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="sunroof_open",
        device_class=BinarySensorDeviceClass.WINDOW,
        value_fn=lambda vehicle: vehicle.sunroof_open,
    ),
    VolvoBinarySensorEntityDescription(
        key="engine_running",
        device_class=BinarySensorDeviceClass.RUNNING,
        value_fn=lambda vehicle: vehicle.engine_running,
    ),
    VolvoBinarySensorEntityDescription(
        key="front_left_window_open",
        device_class=BinarySensorDeviceClass.WINDOW,
        value_fn=lambda vehicle: vehicle.front_left_window_open,
        extra_attributes_fn=lambda vehicle: {"open_status_ajar": vehicle.front_left_window_open_ajar},
    ),
    VolvoBinarySensorEntityDescription(
        key="front_right_window_open",
        device_class=BinarySensorDeviceClass.WINDOW,
        value_fn=lambda vehicle: vehicle.front_right_window_open,
        extra_attributes_fn=lambda vehicle: {"open_status_ajar": vehicle.front_right_window_open_ajar},
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_left_window_open",
        device_class=BinarySensorDeviceClass.WINDOW,
        value_fn=lambda vehicle: vehicle.rear_left_window_open,
        extra_attributes_fn=lambda vehicle: {"open_status_ajar": vehicle.rear_left_window_open_ajar},
    ),
    VolvoBinarySensorEntityDescription(
        key="rear_right_window_open",
        device_class=BinarySensorDeviceClass.WINDOW,
        value_fn=lambda vehicle: vehicle.rear_right_window_open,
        extra_attributes_fn=lambda vehicle: {"open_status_ajar": vehicle.rear_right_window_open_ajar},
    ),
    DIAGNOSTIC_PROBLEM,
    *WARNING_DESCRIPTIONS,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoBinarySensor] = []

    for vehicle in coordinator.data:
        for description in BINARY_SENSOR_DESCRIPTIONS:
            entities.append(VolvoBinarySensor(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoBinarySensor(VolvoEntity, BinarySensorEntity):
    entity_description: VolvoBinarySensorEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoBinarySensorEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def is_on(self) -> bool | None:
        return self.entity_description.value_fn(self.vehicle)

    @property
    def extra_state_attributes(self) -> Mapping[str, bool] | None:
        if self.entity_description.extra_attributes_fn is None:
            return None
        return self.entity_description.extra_attributes_fn(self.vehicle)
