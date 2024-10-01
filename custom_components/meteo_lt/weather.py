"""Weather platform for Meteo.lt integration."""
import logging
from typing import Any, Dict, Optional

from homeassistant.components.weather import WeatherEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    TEMP_CELSIUS,
    PRESSURE_HPA,
    SPEED_METERS_PER_SECOND,
    PERCENTAGE,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up Meteo.lt weather based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([MeteoLtWeather(coordinator, entry)], False)

class MeteoLtWeather(CoordinatorEntity, WeatherEntity):
    """Representation of Meteo.lt weather data."""

    def __init__(self, coordinator: DataUpdateCoordinator, config_entry: ConfigEntry) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._config_entry = config_entry

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"Meteo.lt Weather {self._config_entry.data['location']}"

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self._config_entry.entry_id}"

    @property
    def condition(self) -> Optional[str]:
        """Return the current condition."""
        return self.coordinator.data["forecastTimestamps"][0]["conditionCode"]

    @property
    def temperature(self) -> Optional[float]:
        """Return the temperature."""
        return self.coordinator.data["forecastTimestamps"][0]["airTemperature"]

    @property
    def temperature_unit(self) -> str:
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def humidity(self) -> Optional[float]:
        """Return the humidity."""
        return self.coordinator.data["forecastTimestamps"][0]["relativeHumidity"]

    @property
    def wind_speed(self) -> Optional[float]:
        """Return the wind speed."""
        return self.coordinator.data["forecastTimestamps"][0]["windSpeed"]

    @property
    def wind_bearing(self) -> Optional[float]:
        """Return the wind bearing."""
        return self.coordinator.data["forecastTimestamps"][0]["windDirection"]

    @property
    def pressure(self) -> Optional[float]:
        """Return the pressure."""
        return self.coordinator.data["forecastTimestamps"][0]["seaLevelPressure"]

    @property
    def attribution(self) -> str:
        """Return the attribution."""
        return "Data provided by Meteo.lt"
