from homeassistant import config_entries

DOMAIN = "volvooncall_cn"

class VolvoOnCallCnConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1

    async def async_step_user(self, info):
        if info is not None:
            pass  # TODO: process info

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(
                {
                    vol.Required("username"): str,
                    vol.Required("password"): str
                })
        )
