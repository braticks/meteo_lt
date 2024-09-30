# Meteo.lt Integration for Home Assistant

This custom integration allows you to integrate weather data from the Lithuanian Hydrometeorological Service (Meteo.lt) into your Home Assistant instance.

## Features

- Real-time weather data for Lithuanian locations
- Temperature, humidity, wind speed, and weather condition sensors
- Weather entity for a comprehensive weather overview
- Configurable location

## Configuration

1. In Home Assistant, go to Configuration > Integrations.
2. Click the "+ ADD INTEGRATION" button.
3. Search for "Meteo.lt" and select it.
4. Enter the desired location (e.g., "vilnius", "kaunas", "klaipeda").
5. Click "Submit".

## Available Entities

- `weather.meteo_lt_[location]`: Weather entity with overall weather information
- `sensor.meteo_lt_temperature`: Current temperature
- `sensor.meteo_lt_humidity`: Current humidity
- `sensor.meteo_lt_wind_speed`: Current wind speed

{% if installed %}
## Changes

### [Version number or date of the latest update]
- [List of changes or new features]

{% endif %}
