from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from homeassistant.components.device_tracker import SourceType
from homeassistant.components.device_tracker.config_entry import TrackerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import Vehicle


@dataclass(frozen=True, kw_only=True)
class VolvoTrackerEntityDescription(EntityDescription):
    location_fn: Callable[[Vehicle], dict[str, float]]


TRACKER_DESCRIPTIONS: tuple[VolvoTrackerEntityDescription, ...] = (
    VolvoTrackerEntityDescription(
        key="position",
        location_fn=lambda vehicle: vehicle.position,
    ),
    VolvoTrackerEntityDescription(
        key="position_wgs84",
        location_fn=lambda vehicle: vehicle.position_wgs84,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: VolvoCoordinator = config_entry.runtime_data.coordinator
    entities: list[VolvoTracker] = []

    for vehicle in coordinator.data:
        for description in TRACKER_DESCRIPTIONS:
            entities.append(VolvoTracker(coordinator, vehicle, description))

    async_add_entities(entities)


class VolvoTracker(VolvoEntity, TrackerEntity):
    entity_description: VolvoTrackerEntityDescription

    def __init__(
        self,
        coordinator: VolvoCoordinator,
        vehicle: Vehicle,
        description: VolvoTrackerEntityDescription,
    ) -> None:
        super().__init__(coordinator, vehicle, description)

    @property
    def source_type(self) -> SourceType:
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        location = self.entity_description.location_fn(self.vehicle)
        return location.get("latitude") if location else None

    @property
    def longitude(self) -> float | None:
        location = self.entity_description.location_fn(self.vehicle)
        return location.get("longitude") if location else None
