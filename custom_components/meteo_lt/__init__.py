"""The Meteo.lt integration."""
import asyncio
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "weather"]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Meteo.lt component."""
    _LOGGER.debug("Setting up Meteo.lt component")
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Meteo.lt from a config entry."""
    _LOGGER.debug("Setting up Meteo.lt entry: %s", entry.data)
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.debug("Unloading Meteo.lt entry: %s", entry.data)
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
