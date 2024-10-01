"""DataUpdateCoordinator for meteo_lt."""
from datetime import timedelta
import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

class MeteoLtDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Meteo.lt data."""

    def __init__(self, hass: HomeAssistant, location: str):
        """Initialize."""
        super().__init__(
            hass,
            hass.data[DOMAIN],
            name=DOMAIN,
            update_interval=timedelta(minutes=10),
        )
        self.location = location

    async def _async_update_data(self):
        """Fetch data from Meteo.lt."""
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(f"https://api.meteo.lt/v1/places/{self.location}/forecasts/long-term") as response:
                if response.status != 200:
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                return await response.json()
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
