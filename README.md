# Meteo.lt Integration for Home Assistant

[English version below](#meteo-lt-integration-for-home-assistant-1)

## Meteo.lt integracija Home Assistant sistemai

Ši integracija leidžia gauti orų prognozes iš Meteo.lt paslaugos jūsų Home Assistant sistemoje.

### Galimos vietovės

Integracija palaiko visas vietoves, kurias teikia Meteo.lt API. Kai kurios populiariausios vietovės:

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

Pilną vietovių sąrašą galite rasti [Meteo.lt API dokumentacijoje](https://api.meteo.lt/#places).

### Prieinami jutikliai

Integracija sukuria šiuos jutiklius:

1. Temperatūra (°C)
2. Drėgmė (%)
3. Vėjo greitis (m/s)
4. Oro sąlygos (aprašymas)

Be to, sukuriamas orų objektas, kuris apjungia visą informaciją į vieną esybę.

### Diegimas

1. Įdiekite šią integraciją naudodami HACS arba rankiniu būdu nukopijuodami failus į savo `custom_components` aplanką.
2. Perkraukite Home Assistant.
3. Eikite į Integracijos ir pridėkite naują Meteo.lt integraciją.
4. Įveskite norimą vietovę.

### Naudojimas

Po sėkmingo diegimo, galėsite naudoti Meteo.lt duomenis savo prietaisų skydeliuose, automatizacijose ir skriptuose.

---

## Meteo.lt Integration for Home Assistant

This integration allows you to get weather forecasts from the Meteo.lt service in your Home Assistant system.

### Available Locations

The integration supports all locations provided by the Meteo.lt API. Some of the most popular locations include:

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

For a full list of locations, please refer to the [Meteo.lt API documentation](https://api.meteo.lt/#places).

### Available Sensors

The integration creates the following sensors:

1. Temperature (°C)
2. Humidity (%)
3. Wind Speed (m/s)
4. Weather Condition (description)

Additionally, a weather entity is created that combines all this information into a single entity.

### Installation

1. Install this integration using HACS or manually by copying the files to your `custom_components` folder.
2. Restart Home Assistant.
3. Go to Integrations and add a new Meteo.lt integration.
4. Enter the desired location.

### Usage

After successful installation, you will be able to use Meteo.lt data in your dashboards, automations, and scripts.
