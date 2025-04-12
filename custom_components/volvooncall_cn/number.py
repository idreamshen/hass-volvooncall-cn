import logging
from propcache import cached_property
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.number import NumberEntity
from homeassistant.const import Platform
from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import DOMAIN

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
        super().__init__(coordinator, idx, metaMapKey, Platform.NUMBER)
        self.max_duration = 15
        self.min_duration = 1

    @cached_property
    def native_max_value(self) -> float:
        return self.max_duration

    @cached_property
    def native_min_value(self) -> float:
        return self.min_duration

    @cached_property
    def native_step(self) -> float:
        return 1

    @cached_property
    def native_value(self):
       store_data = self.coordinator.store_datas[self.idx]
       return store_data.get_engine_duration_number()

    @property
    def state(self):
        store_data = self.coordinator.store_datas[self.idx]
        return store_data.get_engine_duration_number()

    async def async_set_native_value(self, value):
        store_data = self.coordinator.store_datas[self.idx]
        await store_data.set_engine_duration_number(value)
        await self.coordinator.async_refresh()
