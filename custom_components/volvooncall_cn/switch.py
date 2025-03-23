import logging
import asyncio
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.switch import SwitchEntity

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_cn import DOMAIN
from .volvooncall_base import MAX_RETRIES

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up button."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    switchs = []
    for idx, _ in enumerate(coordinator.data):
        switchs.append(VolvoEngineSwitch(coordinator, idx, "engine_switch"))

    async_add_entities(switchs)


class VolvoEngineSwitch(VolvoEntity, SwitchEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    async def _update_status(self, is_on):
        for _ in range(MAX_RETRIES):
            await asyncio.sleep(2)
            await self.coordinator.async_refresh()
            if self.is_on == is_on:
                break

    async def async_turn_on(self) -> None:
        await self.coordinator.data[self.idx].engine_start()
        await self._update_status(True)

    async def async_turn_off(self) -> None:
        await self.coordinator.data[self.idx].engine_stop()
        await self._update_status(False)

    @property
    def is_on(self):
        coordinator = self.coordinator.data[self.idx]
        return coordinator.get("engine_running") or coordinator.get("engine_remote_running")
