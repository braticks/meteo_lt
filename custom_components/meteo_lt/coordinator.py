"""DataUpdateCoordinator for meteo_lt."""
import logging
from datetime import timedelta
import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class MeteoLtDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo.lt data."""

    def __init__(self, hass: HomeAssistant, location: str):
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=10),
        )
        self.location = location
        _LOGGER.debug("Initializing coordinator for location: %s", location)

    async def _async_update_data(self):
        """Fetch data from Meteo.lt."""
        session = async_get_clientsession(self.hass)
        url = f"https://api.meteo.lt/v1/places/{self.location}/forecasts/long-term"
        _LOGGER.debug("Fetching data from: %s", url)
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    _LOGGER.error("Error fetching data: %s", response.status)
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                data = await response.json()
                _LOGGER.debug("Received data: %s", data)
                return data
        except aiohttp.ClientError as err:
            _LOGGER.error("Error communicating with API: %s", err)
            raise UpdateFailed(f"Error communicating with API: {err}")
