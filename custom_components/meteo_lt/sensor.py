"""Sensor platform for Meteo.lt integration."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Meteo.lt sensor entries."""
    location = entry.data["location"]
    async_add_entities([
        MeteoLtTemperatureSensor(location),
        MeteoLtHumiditySensor(location),
        MeteoLtWindSpeedSensor(location),
    ])

class MeteoLtTemperatureSensor(SensorEntity):
    """Representation of a Meteo.lt temperature sensor."""
    # Implement sensor logic here

class MeteoLtHumiditySensor(SensorEntity):
    """Representation of a Meteo.lt humidity sensor."""
    # Implement sensor logic here

class MeteoLtWindSpeedSensor(SensorEntity):
    """Representation of a Meteo.lt wind speed sensor."""
    # Implement sensor logic here
