"""Constants for the Meteo.lt integration."""

from homeassistant.helpers.update_coordinator import UpdateFailed

DOMAIN = "meteo_lt"
CONF_LOCATION = "location"
DEFAULT_LOCATION = "vilnius"

LOCATION_ERROR = "invalid_location"
CONNECTION_ERROR = "cannot_connect"
