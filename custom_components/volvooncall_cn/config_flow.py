import logging

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import voluptuous as vol
from .volvooncall_cn import VehicleAPI, Vehicle, VolvoAPIError
DOMAIN = "volvooncall_cn"

_LOGGER = logging.getLogger(__name__)


class VolvoOnCallCnConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1

    async def async_step_user(self, user_input):
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input["username"])

            session = async_get_clientsession(self.hass)
            my_api = VehicleAPI(session=session, username=user_input["username"], password=user_input["password"])
            try:
                await my_api.login()
            except VolvoAPIError as err:
                errors["base"] = err.message
            except Exception:
                _LOGGER.exception("Unhandled exception in user step")
                errors["base"] = "unknown"

            if not errors:
                return self.async_create_entry(
                    title=user_input["username"], data=user_input
                )

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {
                    vol.Required("username"): int,
                    vol.Required("password"): str
                }), errors=errors
        )
