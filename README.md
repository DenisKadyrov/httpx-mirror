# httpx-mirror

🛰️ Minimal async HTTP proxy that logs and replays requests for debugging and analysis.

## Features

- [ ] Async proxy endpoint for any HTTP method
- [ ] Logging full request/response to SQLite
- [ ] Replay previously recorded requests
- [ ] CLI interface (via Typer)
- [ ] Metrics and stats API (latency, status codes)
- [ ] Filtering and export

## Project Goal

This project is designed to help understand async architecture, HTTP proxying, and request lifecycle in real systems — while staying minimal and readable (KISS).

## Usage

```bash
uvicorn app.main:app
curl -X POST http://localhost:8000/proxy?target=https://httpbin.org/post

