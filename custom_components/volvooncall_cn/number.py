import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.number import NumberEntity
from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import DOMAIN
from propcache import cached_property

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up button."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    numbers = []
    for idx, _ in enumerate(coordinator.data):
        numbers.append(VolovEngineDurationNumInput(coordinator, idx, "engine_duration_number"))

    async_add_entities(numbers)


class VolovEngineDurationNumInput(VolvoEntity, NumberEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)
        self.max_duration = 15
        self.min_duration = 1

    @property
    def max_value(self) -> float:
        return self.max_duration

    @cached_property
    def native_max_value(self) -> float:
        return self.max_duration

    @property
    def min_value(self):
        return self.min_duration

    @cached_property
    def native_min_value(self) -> float:
        return self.min_duration

    @property
    def step(self):
        return 1

    @cached_property
    def native_step(self) -> float:
        return 1

    @property
    def value(self):
        return self.coordinator.data[self.idx].get_engine_duration()

    async def async_set_value(self, value):
        await self.coordinator.data[self.idx].set_engine_duration(value)
        await self.coordinator.async_refresh()
