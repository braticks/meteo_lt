"""Sensor platform for Meteo.lt integration."""
import logging
import aiohttp
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator, UpdateFailed
from datetime import timedelta

from .const import DOMAIN, CONF_LOCATION

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Meteo.lt sensor entries."""
    location = entry.data[CONF_LOCATION]
    _LOGGER.debug("Setting up Meteo.lt sensors for location: %s", location)

    coordinator = MeteoLtDataUpdateCoordinator(hass, location)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([
        MeteoLtTemperatureSensor(coordinator),
        MeteoLtHumiditySensor(coordinator),
        MeteoLtWindSpeedSensor(coordinator)
    ])

class MeteoLtDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo.lt data."""

    def __init__(self, hass: HomeAssistant, location: str):
        """Initialize."""
        self.location = location
        update_interval = timedelta(minutes=10)
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self):
        """Fetch data from Meteo.lt."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.meteo.lt/v1/places/{self.location}/forecasts/long-term") as response:
                if response.status != 200:
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                return await response.json()

class MeteoLtSensor(CoordinatorEntity, SensorEntity):
    """Base class for Meteo.lt sensor."""

    def __init__(self, coordinator: MeteoLtDataUpdateCoordinator):
        """Initialize the sensor."""
        super().__init__(coordinator)

class MeteoLtTemperatureSensor(MeteoLtSensor):
    """Representation of a Meteo.lt temperature sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Meteo.lt Temperature"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data["forecastTimestamps"][0]["airTemperature"]

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "°C"

class MeteoLtHumiditySensor(MeteoLtSensor):
    """Representation of a Meteo.lt humidity sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Meteo.lt Humidity"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data["forecastTimestamps"][0]["relativeHumidity"]

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "%"

class MeteoLtWindSpeedSensor(MeteoLtSensor):
    """Representation of a Meteo.lt wind speed sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Meteo.lt Wind Speed"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data["forecastTimestamps"][0]["windSpeed"]

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "m/s"
