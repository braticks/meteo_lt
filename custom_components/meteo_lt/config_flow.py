"""Config flow for Meteo.lt integration."""
import voluptuous as vol
import requests

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, CONF_LOCATION, CONNECTION_ERROR, LOCATION_ERROR

def get_available_locations():
    """Get available locations from Meteo.lt API."""
    try:
        response = requests.get("https://api.meteo.lt/v1/places")
        if response.status_code == 200:
            places = response.json()
            return {place['code']: place['name'] for place in places}
        else:
            return None
    except requests.RequestException:
        return None

class MeteoLtConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteo.lt."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        locations = await self.hass.async_add_executor_job(get_available_locations)

        if locations is None:
            errors["base"] = CONNECTION_ERROR

        if user_input is not None:
            if user_input[CONF_LOCATION] in locations:
                return self.async_create_entry(
                    title=locations[user_input[CONF_LOCATION]],
                    data=user_input
                )
            else:
                errors[CONF_LOCATION] = LOCATION_ERROR

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_LOCATION): vol.In(locations or {})
            }),
            errors=errors,
        )
