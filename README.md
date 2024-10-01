# Meteo.lt Integration for Home Assistant

[English version below](#meteo-lt-integration-for-home-assistant-1)

## Meteo.lt integracija Home Assistant sistemai

Ši integracija leidžia jums gauti orų prognozes iš Meteo.lt jūsų Home Assistant sistemoje.

### Funkcijos

- Rodo dabartinę temperatūrą
- Rodo oro drėgnumą
- Rodo vėjo greitį
- Rodo bendrą oro sąlygų būseną

### Prieinami jutikliai

1. Temperatūra (°C)
2. Santykinis oro drėgnumas (%)
3. Vėjo greitis (m/s)
4. Oro sąlygų būsena (aprašymas)

### Prieinamos vietovės

Integracija palaiko visas Meteo.lt teikiamas vietoves, įskaitant (bet neapsiribojant):

- Vilnius
- Kaunas
- Klaipėda
- Šiauliai
- Panevėžys
- Alytus
- Marijampolė
- Mažeikiai
- Jonava
- Utena

Pilną vietovių sąrašą galite rasti [Meteo.lt API dokumentacijoje](https://api.meteo.lt/).

### Diegimas

1. Įdiekite šią integraciją naudodami HACS (Home Assistant Community Store):
   - HACS -> Integracijos -> Pridėti repozitoriją
   - Įveskite: `https://github.com/braticks/meteo_lt`
2. Perkraukite Home Assistant.
3. Eikite į Konfigūracija -> Integracijos -> Pridėti integraciją
4. Ieškokite "Meteo.lt" ir pasirinkite ją.
5. Įveskite norimą vietovę (pvz., "Vilnius", "Kaunas", "Klaipėda" ir t.t.).

### Konfigūracija

Šiai integracijai nereikia jokios papildomos konfigūracijos `configuration.yaml` faile. Visa konfigūracija atliekama per vartotojo sąsają.

### Palaikymas

Jei turite klausimų ar susiduriate su problemomis, prašome atidaryti naują problemą (issue) GitHub repozitorijoje.

---

## Meteo.lt Integration for Home Assistant

This integration allows you to get weather forecasts from Meteo.lt in your Home Assistant system.

### Features

- Displays current temperature
- Displays humidity
- Displays wind speed
- Displays overall weather condition

### Available Sensors

1. Temperature (°C)
2. Relative Humidity (%)
3. Wind Speed (m/s)
4. Weather Condition (description)

### Available Locations

The integration supports all locations provided by Meteo.lt, including (but not limited to):

- Vilnius
- Kaunas
- Klaipėda
- Šiauliai
- Panevėžys
- Alytus
- Marijampolė
- Mažeikiai
- Jonava
- Utena

For a complete list of locations, please refer to the [Meteo.lt API documentation](https://api.meteo.lt/).

### Installation

1. Install this integration using HACS (Home Assistant Community Store):
   - HACS -> Integrations -> Add Repository
   - Enter: `https://github.com/braticks/meteo_lt`
2. Restart Home Assistant.
3. Go to Configuration -> Integrations -> Add Integration
4. Search for "Meteo.lt" and select it.
5. Enter the desired location (e.g., "Vilnius", "Kaunas", "Klaipeda", etc.).

### Configuration

This integration doesn't require any additional configuration in the `configuration.yaml` file. All configuration is done through the user interface.

### Support

If you have any questions or encounter any issues, please open a new issue on the GitHub repository.
