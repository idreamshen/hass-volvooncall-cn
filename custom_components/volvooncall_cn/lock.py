from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable

from homeassistant.components.lock import LockEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_base import MAX_RETRIES
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoLockEntityDescription(EntityDescription):
    is_locked_fn: Callable[[Vehicle], bool | None]
    lock_fn: Callable[[Vehicle], Awaitable[None]]
    unlock_fn: Callable[[Vehicle], Awaitable[None]]
    available_fn: Callable[[Vehicle], bool] | None = None


LOCK_DESCRIPTIONS: tuple[VolvoLockEntityDescription, ...] = (
    VolvoLockEntityDescription(
        key="car_lock",
        is_locked_fn=lambda vehicle: vehicle.car_locked,
        lock_fn=lambda vehicle: vehicle.lock_vehicle(),
        unlock_fn=lambda vehicle: vehicle.unlock_vehicle(),
    ),
    VolvoLockEntityDescription(
        key="window_lock",
        is_locked_fn=lambda vehicle: _window_is_locked(vehicle),
        lock_fn=lambda vehicle: vehicle.lock_window(),
        unlock_fn=lambda vehicle: vehicle.unlock_window(),
        available_fn=lambda vehicle: vehicle.isAaos,
    ),
)


def _window_is_locked(vehicle: Vehicle) -> bool | None:
    window_states = [
        vehicle.front_left_window_open,
        vehicle.front_right_window_open,
        vehicle.rear_right_window_open,
        vehicle.rear_left_window_open,
    ]
    if any(state is None for state in window_states):
        return None
    return not any(window_states)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoLock] = []

    for vehicle in coordinator.data:
        for description in LOCK_DESCRIPTIONS:
            if description.available_fn and not description.available_fn(vehicle):
                continue
            entities.append(VolvoLock(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoLock(VolvoEntity, LockEntity):
    entity_description: VolvoLockEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoLockEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def is_locked(self) -> bool | None:
        return self.entity_description.is_locked_fn(self.vehicle)

    async def _update_status(self, is_locked: bool) -> None:
        for _ in range(MAX_RETRIES):
            await asyncio.sleep(1)
            await self.coordinator.async_request_refresh()
            if self.is_locked == is_locked:
                break

    async def async_lock(self, **kwargs) -> None:
        await self.entity_description.lock_fn(self.vehicle)
        await self._update_status(True)

    async def async_unlock(self, **kwargs) -> None:
        await self.entity_description.unlock_fn(self.vehicle)
        await self._update_status(False)
