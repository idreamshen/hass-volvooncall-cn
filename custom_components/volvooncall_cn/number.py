from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable

from homeassistant.components.number import NumberEntity, NumberEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTime
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[VolvoCoordinator, Vehicle], float]
    set_value_fn: Callable[[VolvoCoordinator, Vehicle, float], Awaitable[None]]


NUMBER_DESCRIPTIONS: tuple[VolvoNumberEntityDescription, ...] = (
    VolvoNumberEntityDescription(
        key="engine_duration_number",
        native_min_value=1,
        native_max_value=15,
        native_step=1,
        native_unit_of_measurement=UnitOfTime.MINUTES,
        value_fn=lambda coordinator, vehicle: coordinator.stores[vehicle.vin].get_engine_duration_number(),
        set_value_fn=lambda coordinator, vehicle, value: coordinator.stores[vehicle.vin].set_engine_duration_number(value),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoNumber] = []

    for vehicle in coordinator.data:
        for description in NUMBER_DESCRIPTIONS:
            entities.append(VolvoNumber(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoNumber(VolvoEntity, NumberEntity):
    entity_description: VolvoNumberEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoNumberEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def native_value(self) -> float | None:
        return self.entity_description.value_fn(self.coordinator, self.vehicle)

    async def async_set_native_value(self, value: float) -> None:
        await self.entity_description.set_value_fn(self.coordinator, self.vehicle, value)
        await self.coordinator.async_request_refresh()
