from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable, Mapping

from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_base import MAX_RETRIES
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[Vehicle], bool]
    turn_on_fn: Callable[[VolvoCoordinator, Vehicle], Awaitable[None]]
    turn_off_fn: Callable[[VolvoCoordinator, Vehicle], Awaitable[None]]
    extra_attributes_fn: Callable[[Vehicle], Mapping[str, int] | None] | None = None
    available_fn: Callable[[Vehicle], bool] | None = None


SWITCH_DESCRIPTIONS: tuple[VolvoSwitchEntityDescription, ...] = (
    VolvoSwitchEntityDescription(
        key="engine_switch",
        is_on_fn=lambda vehicle: vehicle.engine_running or vehicle.engine_remote_running,
        turn_on_fn=lambda coordinator, vehicle: vehicle.engine_start(
            coordinator.stores[vehicle.vin].get_engine_duration_number()
        ),
        turn_off_fn=lambda coordinator, vehicle: vehicle.engine_stop(),
        extra_attributes_fn=lambda vehicle: {
            "remote_start_at": vehicle.engine_remote_start_time,
            "remote_end_at": vehicle.engine_remote_end_time,
        },
    ),
    VolvoSwitchEntityDescription(
        key="tail_gate_switch",
        is_on_fn=lambda vehicle: vehicle.tail_gate_open,
        turn_on_fn=lambda coordinator, vehicle: _tailgate_open(vehicle),
        turn_off_fn=lambda coordinator, vehicle: vehicle.tail_gate_control_close(),
        available_fn=lambda vehicle: vehicle.isAaos,
    ),
    VolvoSwitchEntityDescription(
        key="sunroof_switch",
        is_on_fn=lambda vehicle: vehicle.sunroof_open,
        turn_on_fn=lambda coordinator, vehicle: vehicle.sunroof_control_open(),
        turn_off_fn=lambda coordinator, vehicle: vehicle.sunroof_control_close(),
        available_fn=lambda vehicle: vehicle.isAaos,
    ),
)


async def _tailgate_open(vehicle: Vehicle) -> None:
    await vehicle.unlock_vehicle_trunk_only()
    await vehicle.tail_gate_control_open()


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoSwitch] = []

    for vehicle in coordinator.data:
        for description in SWITCH_DESCRIPTIONS:
            if description.available_fn and not description.available_fn(vehicle):
                continue
            entities.append(VolvoSwitch(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoSwitch(VolvoEntity, SwitchEntity):
    entity_description: VolvoSwitchEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoSwitchEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def is_on(self) -> bool:
        return self.entity_description.is_on_fn(self.vehicle)

    @property
    def extra_state_attributes(self) -> Mapping[str, int] | None:
        if self.entity_description.extra_attributes_fn is None:
            return None
        return self.entity_description.extra_attributes_fn(self.vehicle)

    async def _update_status(self, is_on: bool) -> None:
        for _ in range(MAX_RETRIES):
            await asyncio.sleep(2)
            await self.coordinator.async_request_refresh()
            if self.is_on == is_on:
                break

    async def async_turn_on(self) -> None:
        await self.entity_description.turn_on_fn(self.coordinator, self.vehicle)
        await self._update_status(True)

    async def async_turn_off(self) -> None:
        await self.entity_description.turn_off_fn(self.coordinator, self.vehicle)
        await self._update_status(False)
