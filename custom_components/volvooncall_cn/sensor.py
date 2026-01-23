from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory, UnitOfLength, UnitOfVolume
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Vehicle], StateType | None]


SENSOR_DESCRIPTIONS: tuple[VolvoSensorEntityDescription, ...] = (
    VolvoSensorEntityDescription(
        key="distance_to_empty",
        device_class=SensorDeviceClass.DISTANCE,
        native_unit_of_measurement=UnitOfLength.KILOMETERS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda vehicle: vehicle.distance_to_empty,
    ),
    VolvoSensorEntityDescription(
        key="odo_meter",
        device_class=SensorDeviceClass.DISTANCE,
        native_unit_of_measurement=UnitOfLength.KILOMETERS,
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda vehicle: vehicle.odo_meter,
    ),
    VolvoSensorEntityDescription(
        key="fuel_amount",
        device_class=SensorDeviceClass.VOLUME,
        native_unit_of_measurement=UnitOfVolume.LITERS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda vehicle: vehicle.fuel_amount,
    ),
    VolvoSensorEntityDescription(
        key="fuel_average_consumption_liters_per_100_km",
        native_unit_of_measurement="L/100km",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda vehicle: vehicle.fuel_average_consumption_liters_per_100_km,
    ),
    VolvoSensorEntityDescription(
        key="service_warning_msg",
        device_class=SensorDeviceClass.ENUM,
        options=[str(value) for value in range(12)],
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda vehicle: str(vehicle.service_warning_msg),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoSensor] = []

    for vehicle in coordinator.data:
        for description in SENSOR_DESCRIPTIONS:
            entities.append(VolvoSensor(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoSensor(VolvoEntity, SensorEntity):
    entity_description: VolvoSensorEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoSensorEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def native_value(self) -> StateType | None:
        return self.entity_description.value_fn(self.vehicle)
