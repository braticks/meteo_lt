"""Config flow for Meteo.lt integration."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN, CONF_LOCATION

class MeteoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteo.lt."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_LOCATION])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_LOCATION], data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_LOCATION): str
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return MeteoLtOptionsFlow(config_entry)

class MeteoLtOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Meteo.lt."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_LOCATION, default=self.config_entry.data.get(CONF_LOCATION)): str
            })
        )
