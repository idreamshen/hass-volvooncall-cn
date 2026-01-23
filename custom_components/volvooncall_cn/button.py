from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Vehicle], Awaitable[None]]


BUTTON_DESCRIPTIONS: tuple[VolvoButtonEntityDescription, ...] = (
    VolvoButtonEntityDescription(
        key="flash_button",
        press_fn=lambda vehicle: vehicle.flash(),
    ),
    VolvoButtonEntityDescription(
        key="honk_flash_button",
        press_fn=lambda vehicle: vehicle.honk_and_flash(),
    ),
    VolvoButtonEntityDescription(
        key="honk_button",
        press_fn=lambda vehicle: vehicle.honk(),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoButton] = []

    for vehicle in coordinator.data:
        for description in BUTTON_DESCRIPTIONS:
            entities.append(VolvoButton(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoButton(VolvoEntity, ButtonEntity):
    entity_description: VolvoButtonEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoButtonEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    async def async_press(self) -> None:
        await self.entity_description.press_fn(self.vehicle)
