import logging

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_SCAN_INTERVAL, CONF_USERNAME
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import voluptuous as vol

from .const import DOMAIN
from .volvooncall_base import DEFAULT_SCAN_INTERVAL, VolvoAPIError
from .volvooncall_cn import VehicleAPI

_LOGGER = logging.getLogger(__name__)


async def volvo_validation(hass, username, password) -> dict:
    errors = {}
    session = async_get_clientsession(hass)
    try:
        volvo_api = VehicleAPI(
            session=session, username=username, password=password)
        await volvo_api.login()
    except VolvoAPIError as err:
        errors["base"] = err.message
    except Exception:
        _LOGGER.exception("Unhandled exception in user step")
        errors["base"] = "unknown"
    return errors


class VolvoOnCallCnConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 2

    @staticmethod
    @callback
    def async_get_options_flow(entry: config_entries.ConfigEntry):
        return VolvoOnCallCnOptionsFlow(entry)

    async def async_step_user(self, user_input):
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_USERNAME])
            self._abort_if_unique_id_configured()
            username = user_input.get(CONF_USERNAME, "")
            password = user_input.get(CONF_PASSWORD, "")
            scan_interval = user_input.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
            errors = await volvo_validation(self.hass, username, password)
            if not errors:
                return self.async_create_entry(
                    title=username,
                    data={
                        CONF_USERNAME: username,
                        CONF_PASSWORD: password,
                    },
                    options={
                        CONF_SCAN_INTERVAL: scan_interval,
                    },
                )
        config_schema = vol.Schema({
            vol.Required(CONF_USERNAME): str,
            vol.Required(CONF_PASSWORD): str,
            vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): vol.All(vol.Coerce(int), vol.Range(min=5)),
        })
        return self.async_show_form(step_id="user", data_schema=config_schema, errors=errors)


class VolvoOnCallCnOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        scan_interval = self.config_entry.options.get(
            CONF_SCAN_INTERVAL,
            self.config_entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
        )
        config_schema = vol.Schema({
            vol.Optional(CONF_SCAN_INTERVAL, default=scan_interval): vol.All(vol.Coerce(int), vol.Range(min=5)),
        })
        return self.async_show_form(step_id="user", data_schema=config_schema, errors={})
