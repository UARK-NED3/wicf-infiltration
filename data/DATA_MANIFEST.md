# Data manifest

| Path | Class | Description | Source and retrieval | Rights/status | SHA-256 |
|---|---|---|---|---|---|
| `raw/bentonville_ar_2025_daily_weather.json` | Public reanalysis input | Daily 2 m mean temperature and RH for 36.3729 N, 94.2088 W (nearest returned grid cell is recorded in the file). Used only for climate sensitivity. | Open-Meteo Archive API request, retrieved 2026-08-19: <https://archive-api.open-meteo.com/v1/archive?latitude=36.3729&longitude=-94.2088&start_date=2025-01-01&end_date=2025-12-31&daily=temperature_2m_mean,relative_humidity_2m_mean&timezone=America%2FChicago> | External data; preserve provider attribution/terms. It is not facility measurement data. | `3b406624b69fa66348326952fd1216cffbc3a5bfe5a634aa04872753d57f881d` |

The 2025 weather file is a reproducible public sensitivity input. It must not be interpreted as the temperature/humidity in a Walmart or HFA inventory room.
