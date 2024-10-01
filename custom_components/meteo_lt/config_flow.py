"""Config flow for Meteo.lt integration."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import aiohttp

from .const import DOMAIN, CONF_LOCATION, API_ENDPOINT

class MeteoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteo.lt."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_LOCATION], data=user_input)

        locations = await self._get_locations()
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_LOCATION): vol.In(locations)
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def _get_locations(self):
        """Fetch locations from the Meteo.lt API."""
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(API_ENDPOINT) as response:
                data = await response.json()
                return {place['code']: place['name'] for place in data}
        except aiohttp.ClientError:
            return {}

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        locations = await self._get_locations()

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_LOCATION, default=self.config_entry.options.get(CONF_LOCATION)): vol.In(locations)
            })
        )

    async def _get_locations(self):
        """Fetch locations from the Meteo.lt API."""
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(API_ENDPOINT) as response:
                data = await response.json()
                return {place['code']: place['name'] for place in data}
        except aiohttp.ClientError:
            return {}
