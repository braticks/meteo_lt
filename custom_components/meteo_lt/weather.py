"""Weather platform for Meteo.lt integration."""
from homeassistant.components.weather import WeatherEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Meteo.lt weather platform."""
    location = entry.data["location"]
    async_add_entities([MeteoLtWeather(location)])

class MeteoLtWeather(WeatherEntity):
    """Representation of a Meteo.lt weather entity."""
    # Implement weather entity logic here
