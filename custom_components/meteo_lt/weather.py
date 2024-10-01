"""Weather platform for Meteo.lt integration."""
import logging
import aiohttp
from homeassistant.components.weather import WeatherEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator, UpdateFailed
from datetime import timedelta

from .const import DOMAIN, CONF_LOCATION

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Meteo.lt weather platform."""
    location = entry.data[CONF_LOCATION]
    coordinator = MeteoLtDataUpdateCoordinator(hass, location)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([MeteoLtWeather(coordinator)])

class MeteoLtDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo.lt data."""

    def __init__(self, hass: HomeAssistant, location: str):
        """Initialize."""
        self.location = location
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=10),
        )

    async def _async_update_data(self):
        """Fetch data from Meteo.lt."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.meteo.lt/v1/places/{self.location}/forecasts/long-term") as response:
                if response.status != 200:
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                return await response.json()

class MeteoLtWeather(CoordinatorEntity, WeatherEntity):
    """Representation of a weather condition."""

    def __init__(self, coordinator: MeteoLtDataUpdateCoordinator):
        """Initialize the weather entity."""
        super().__init__(coordinator)

    @property
    def name(self):
        """Return the name of the weather entity."""
        return "Meteo.lt Weather"

    @property
    def temperature(self):
        """Return the temperature."""
        return self.coordinator.data["forecastTimestamps"][0]["airTemperature"]

    @property
    def humidity(self):
        """Return the humidity."""
        return self.coordinator.data["forecastTimestamps"][0]["relativeHumidity"]

    @property
    def wind_speed(self):
        """Return the wind speed."""
        return self.coordinator.data["forecastTimestamps"][0]["windSpeed"]

    @property
    def condition(self):
        """Return the weather condition."""
        return self.coordinator.data["forecastTimestamps"][0]["conditionCode"]
