from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    location = entry.data["location"]
    async_add_entities([
        MeteoLtTemperatureSensor(location),
        MeteoLtHumiditySensor(location),
        MeteoLtWindSpeedSensor(location),
    ])

class MeteoLtTemperatureSensor(SensorEntity):
    # Implement sensor logic here

class MeteoLtHumiditySensor(SensorEntity):
    # Implement sensor logic here

class MeteoLtWindSpeedSensor(SensorEntity):
    # Implement sensor logic here
