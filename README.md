# Weather Dashboard

A clean, dark-mode weather dashboard that fits on **one screen** (no scrolling) and is built to run full screen. Auto-detects your location and shows current conditions, an hourly forecast, a 7-day forecast, and a live precipitation radar — all from free, no-key APIs. Save favorite locations; your current location is always pinned first.

## Run it locally

Browser geolocation needs `http(s)` (it's blocked on `file://`), so run a tiny local server:

**Option A — double-click (macOS):** open `run-local.command`. It starts a local server and opens the dashboard in your browser. The server sends `Cache-Control: no-store`, so edits to `index.html` always show up on reload (no stale cache).

**Option B — terminal:**

```bash
cd ~/Projects/weather-dashboard
python3 -m http.server 8000
# then open http://localhost:8000
```

Stop the server with `Ctrl+C`.

> **Note:** the plain `python3 -m http.server` lets the browser cache files. If you edit `index.html` and don't see changes, hard-refresh (**Cmd+Shift+R**), or use Option A, which disables caching.

## Features

- **One-screen layout** — current conditions, hourly, 7-day, and radar all visible without scrolling
- **Auto-location** via the browser, with city search
- **Favorites** — search a city and click **☆ Save**; favorites persist in your browser, and your current GPS location is always pinned on top
- **Current conditions:** temperature, condition, feels-like, today's high/low, wind, humidity, UV index, pressure, sunrise, sunset
- **Hourly** (next 24h) with precip chance, **7-day** with highs/lows and rain probability
- **Live radar** (precipitation overlay on a dark base map)
- Dark mode, full-screen toggle, auto-refresh every 10 minutes
- Imperial units (°F, mph, inches)

## Data sources

- [Open-Meteo](https://open-meteo.com) — forecasts (free, no API key)
- [RainViewer](https://rainviewer.com) — radar tiles (free, no API key)
- [BigDataCloud](https://www.bigdatacloud.com) — reverse geocoding (free, no API key)
- [Leaflet](https://leafletjs.com) + [CARTO](https://carto.com) dark base map tiles

## Notes on Weather Underground / AccuWeather

- **Weather Underground:** the public API was discontinued (keys stopped working Feb 2019). Only personal-weather-station owners get limited access. Not usable here.
- **AccuWeather:** has a developer API, but it's separate from any consumer app subscription, and the free tier is ~50 calls/day (too low for auto-refresh). Open-Meteo is used instead — free and hyper-local (1–11 km).

## License

MIT
