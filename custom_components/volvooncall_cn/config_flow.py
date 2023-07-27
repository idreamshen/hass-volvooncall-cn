from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "volvooncall_cn"

class VolvoOnCallCnConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1

    async def async_step_user(self, info):
        if info is not None:
            await self.async_set_unique_id(user_input["username"])
            return self.async_create_entry(
                title=user_input[username], data=user_input
            )

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {
                    vol.Required("username"): str,
                    vol.Required("password"): str
                })
        )
