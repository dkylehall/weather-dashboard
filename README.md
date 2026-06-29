# Weather Dashboard

A clean, dark-mode weather dashboard that runs in any browser and is designed to run full screen. Auto-detects your location and shows current conditions, an hourly forecast, a 7-day forecast, and a live precipitation radar — all from free, no-key APIs.

**Live site:** _enable GitHub Pages to get your URL (Settings → Pages → Deploy from branch → `main` / root)_

## Features

- **Auto-location** via the browser, with city search fallback
- **Current conditions:** temperature, condition, feels-like, today's high/low, wind (speed + direction), humidity, UV index, pressure, sunrise, and sunset
- **Hourly forecast** for the next 24 hours with precipitation chance
- **7-day forecast** with highs/lows and rain probability
- **Live radar** map (precipitation overlay on a dark base map)
- **Dark mode**, responsive layout, full-screen toggle
- **Auto-refreshes** every 10 minutes
- Imperial units (°F, mph, inches)

## Running it

It's a single static file — no build step, no dependencies to install.

- **Locally:** open `index.html` in any browser. (Geolocation is most reliable over `http(s)`; on a `file://` page some browsers block it — use the in-app city search if so.)
- **Hosted (recommended):** serve over HTTPS via GitHub Pages so geolocation works automatically.

## Data sources

- [Open-Meteo](https://open-meteo.com) — forecasts (free, no API key)
- [RainViewer](https://rainviewer.com) — radar tiles (free, no API key)
- [BigDataCloud](https://www.bigdatacloud.com) — reverse geocoding (free, no API key)
- [Leaflet](https://leafletjs.com) + [CARTO](https://carto.com) dark base map tiles

## License

MIT — see [LICENSE](LICENSE).
