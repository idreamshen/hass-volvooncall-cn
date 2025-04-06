import logging
import asyncio
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.switch import SwitchEntity
from homeassistant.const import Platform

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
    for idx, ent in enumerate(coordinator.data):
        switchs.append(VolvoEngineSwitch(coordinator, idx, "engine_switch"))
        if ent.get("isAaos"):
            switchs.append(VolvoTailgateSwitch(coordinator, idx, "tail_gate_switch"))
            switchs.append(VolvoSunroofSwitch(coordinator, idx, "sunroof_switch"))

    async_add_entities(switchs)


class VolvoSwitchEntity(VolvoEntity, SwitchEntity):
    def __init__(self, coordinator, idx, metaKey, checkMetaKeys):
        super().__init__(coordinator, idx, metaKey, Platform.SWITCH)
        self.checkMetaKeys = checkMetaKeys

    async def _update_status(self, is_on):
        for _ in range(MAX_RETRIES):
            await asyncio.sleep(2)
            await self.coordinator.async_refresh()
            if self.is_on == is_on:
                break

    @property
    def is_on(self):
        coordinator = self.coordinator.data[self.idx]
        for key in self.checkMetaKeys:
            if coordinator.get(key):
                return True
        return False


class VolvoEngineSwitch(VolvoSwitchEntity):
    def __init__(self, coordinator, idx, metaKey):
        check_meta_keys = ["engine_running", "engine_remote_running"]
        super().__init__(coordinator, idx, metaKey, check_meta_keys)

    async def async_turn_on(self) -> None:
        await self.coordinator.data[self.idx].engine_start()
        await self._update_status(True)

    async def async_turn_off(self) -> None:
        await self.coordinator.data[self.idx].engine_stop()
        await self._update_status(False)

    @property
    def extra_state_attributes(self):
        start_time = "engine_remote_start_time"
        end_time = "engine_remote_end_time"
        data = self.coordinator.data[self.idx]
        return {
            "remote_start_at": data.get(start_time),
            "remote_end_at": data.get(end_time)
        }


class VolvoTailgateSwitch(VolvoSwitchEntity):
    def __init__(self, coordinator, idx, metaKey):
        check_keys = ["tail_gate_open"]
        super().__init__(coordinator, idx, metaKey, check_keys)

    async def async_turn_on(self) -> None:
        coordinator = self.coordinator.data[self.idx]
        await coordinator.unlock_vehicle_trunk_only()
        await coordinator.tail_gate_control_open()
        await self._update_status(True)

    async def async_turn_off(self) -> None:
        await self.coordinator.data[self.idx].tail_gate_control_close()
        await self._update_status(False)


class VolvoSunroofSwitch(VolvoSwitchEntity):
    def __init__(self, coordinator, idx, metaKey):
        check_keys = ["sunroof_open"]
        super().__init__(coordinator, idx, metaKey, check_keys)

    async def async_turn_on(self) -> None:
        await self.coordinator.data[self.idx].sunroof_control_open()
        await self._update_status(True)

    async def async_turn_off(self) -> None:
        await self.coordinator.data[self.idx].sunroof_control_close()
        await self._update_status(False)
