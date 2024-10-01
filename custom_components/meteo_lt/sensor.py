"""Sensor platform for Meteo.lt integration."""
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import MeteoLtDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up Meteo.lt sensor entries."""
    _LOGGER.debug("Setting up Meteo.lt sensors for entry: %s", entry.entry_id)
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        MeteoLtTemperatureSensor(coordinator, entry),
        MeteoLtHumiditySensor(coordinator, entry),
        MeteoLtWindSpeedSensor(coordinator, entry)
    ]
    
    async_add_entities(entities)
    _LOGGER.debug("Added %d Meteo.lt sensor entities", len(entities))

class MeteoLtSensor(CoordinatorEntity, SensorEntity):
    """Base class for Meteo.lt sensors."""

    def __init__(self, coordinator: MeteoLtDataUpdateCoordinator, config_entry: ConfigEntry):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._config_entry = config_entry
        self._attr_device_info = {
            "identifiers": {(DOMAIN, config_entry.entry_id)},
            "name": f"Meteo.lt {coordinator.location}",
            "manufacturer": "Meteo.lt",
        }

class MeteoLtTemperatureSensor(MeteoLtSensor):
    """Representation of a Meteo.lt temperature sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Meteo.lt Temperature {self.coordinator.location}"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self._config_entry.entry_id}_temperature"

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
        return f"Meteo.lt Humidity {self.coordinator.location}"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self._config_entry.entry_id}_humidity"

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
        return f"Meteo.lt Wind Speed {self.coordinator.location}"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self._config_entry.entry_id}_wind_speed"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data["forecastTimestamps"][0]["windSpeed"]

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "m/s"
