from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.diagnostics import async_redact_data

from .const import DOMAIN

TO_REDACT = {"password", "access_token", "refresh_token", "vocapi_access_token"}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    coordinator = entry.runtime_data.coordinator
    vehicles = []
    for vehicle in coordinator.data:
        vehicles.append(
            {
                "vin": vehicle.vin,
                "series_name": vehicle.series_name,
                "model_name": vehicle.model_name,
                "is_aaos": vehicle.isAaos,
                "nickname": vehicle.nickname,
            }
        )

    return {
        "config_entry": async_redact_data(entry.as_dict(), TO_REDACT),
        "vehicles": vehicles,
        "api": {
            "grpc_channel": coordinator.volvo_api.channel is not None,
            "lbs_channel": coordinator.volvo_api.lbs_channel is not None,
        },
    }


async def async_get_device_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry, device
) -> dict[str, Any]:
    coordinator = entry.runtime_data.coordinator
    vin = next(
        (
            identifier[1]
            for identifier in device.identifiers
            if identifier[0] == DOMAIN
        ),
        None,
    )
    if vin is None:
        return {}

    vehicle = next((item for item in coordinator.data if item.vin == vin), None)
    if vehicle is None:
        return {}

    return {
        "vin": vehicle.vin,
        "series_name": vehicle.series_name,
        "model_name": vehicle.model_name,
        "nickname": vehicle.nickname,
        "availability_status": int(vehicle.availability_status),
        "unavailable_reason": int(vehicle.unavailable_reason),
    }
