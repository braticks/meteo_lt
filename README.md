# Meteo.lt Integration for Home Assistant

This custom integration allows you to integrate weather data from the Lithuanian Hydrometeorological Service (Meteo.lt) into your Home Assistant instance.

## Features

- Real-time weather data for Lithuanian locations
- Temperature, humidity, wind speed, and weather condition sensors
- Weather entity for a comprehensive weather overview
- Configurable location

## Installation

### HACS (Custom Repository)

1. Ensure that [HACS](https://hacs.xyz/) is installed.
2. Go to HACS > Integrations.
3. Click on the three dots in the top right corner and select "Custom repositories".
4. Add the URL of this repository (https://github.com/braticks/meteo_lt) and select "Integration" as the category.
5. Click "Add".
6. Search for "Meteo.lt" in the HACS Integrations store.
7. Click Install.
8. Restart Home Assistant.

### Manual Installation

1. Download the `custom_components/meteo_lt` folder from this repository.
2. Copy the folder into your Home Assistant's `custom_components` directory.
3. Restart Home Assistant.

## Configuration

1. In Home Assistant, go to Configuration > Integrations.
2. Click the "+ ADD INTEGRATION" button.
3. Search for "Meteo.lt" and select it.
4. Enter the desired location (e.g., "vilnius", "kaunas", "klaipeda").
5. Click "Submit".

## Available Entities

After setting up the integration, the following entities will be created:

- `weather.meteo_lt_[location]`: Weather entity with overall weather information
- `sensor.meteo_lt_temperature`: Current temperature
- `sensor.meteo_lt_humidity`: Current humidity
- `sensor.meteo_lt_wind_speed`: Current wind speed

## Troubleshooting

- If you encounter any issues, check the Home Assistant logs for error messages related to the Meteo.lt integration.
- Ensure that you have a stable internet connection.
- Verify that the Meteo.lt API is operational and that you're using a valid location.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the MIT License.

## Disclaimer

This integration is not officially affiliated with or endorsed by the Lithuanian Hydrometeorological Service. Use of the Meteo.lt API is subject to their terms and conditions.

## Support

If you need help or want to report a bug, please open an issue on the GitHub repository.

---

Enjoy your local Lithuanian weather data in Home Assistant!
