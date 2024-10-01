"""Weather platform for Meteo.lt integration."""
from homeassistant.components.weather import WeatherEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import MeteoLtDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up Meteo.lt weather platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([MeteoLtWeather(coordinator)])

class MeteoLtWeather(CoordinatorEntity, WeatherEntity):
    """Representation of a weather condition."""

    def __init__(self, coordinator: MeteoLtDataUpdateCoordinator):
        """Initialize the weather entity."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.location}_weather"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.location)},
            "name": f"Meteo.lt {coordinator.location}",
            "manufacturer": "Meteo.lt",
        }

    @property
    def name(self):
        """Return the name of the weather entity."""
        return f"Meteo.lt Weather {self.coordinator.location}"

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
