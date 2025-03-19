import logging

from homeassistant import config_entries
from homeassistant.const import *
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import voluptuous as vol
from .volvooncall_base import VolvoAPIError
from .volvooncall_cn import VehicleAPI
from .volvooncall_cn import DOMAIN

_LOGGER = logging.getLogger(__name__)


class VolvoOnCallCnConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1

    async def async_step_user(self, user_input):
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_USERNAME])

            session = async_get_clientsession(self.hass)
            volvo_api = VehicleAPI(
                session=session, username=user_input[CONF_USERNAME], password=user_input[CONF_PASSWORD])
            try:
                await volvo_api.login()
            except VolvoAPIError as err:
                errors["base"] = err.message
            except Exception:
                _LOGGER.exception("Unhandled exception in user step")
                errors["base"] = "unknown"

            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_USERNAME], data=user_input
                )

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str
                }), errors=errors
        )
