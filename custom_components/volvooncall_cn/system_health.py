from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import system_health
from homeassistant.helpers.typing import InfoType

from .const import DOMAIN


async def async_register(hass: HomeAssistant) -> None:
    async def system_health_info() -> InfoType:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {}

        entry = entries[0]
        coordinator = entry.runtime_data.coordinator
        return {
            "grpc_connected": coordinator.volvo_api.channel is not None,
            "lbs_grpc_connected": coordinator.volvo_api.lbs_channel is not None,
            "update_interval": str(coordinator.update_interval),
            "vehicle_count": len(coordinator.data),
            "last_update_success": coordinator.last_update_success,
        }

    await system_health.async_register_info(hass, DOMAIN, system_health_info)
