# Lumen API

The HTTP service for Lumen, the AI study co-pilot. Built with FastAPI.

## Run

```bash
# from the repo root
uv run api                      # starts uvicorn (api.app:app)
uv run python -m api            # equivalent
```

Once running:

- API docs (Swagger): http://localhost:8000/docs
- Liveness probe: http://localhost:8000/health
- Versioned API: http://localhost:8000/api/v1

## Configuration

Settings are loaded via `pydantic-settings` from environment variables (prefix
`API_`) and an optional `.env` file. See `.env.example` for the available keys.

## Architecture

Modular (package-by-feature). Each feature is a **self-contained vertical
slice** under `modules/` that owns every layer it needs; shared infrastructure
lives in `core/`. This keeps related code together and lets the surface grow by
adding modules rather than fattening shared layer folders.

```
src/api/
├── app.py            # create_app() factory + the ASGI `app` instance
├── router.py         # assembles feature module routers → /api/v1
├── core/             # cross-cutting infrastructure, shared by all modules
│   ├── config.py     #   settings (pydantic-settings)
│   ├── logging.py    #   logging setup
│   ├── lifespan.py   #   startup/shutdown resource wiring
│   ├── exceptions.py #   base AppError + JSON handlers
│   ├── dependencies.py #  shared FastAPI deps (e.g. SettingsDep)
│   ├── schemas.py    #   shared response models (e.g. Message)
│   └── middleware/   #   ASGI middleware (request id, ...)
└── modules/          # feature modules (one folder per capability)
    └── health/       #   liveness/readiness probes + service metadata
        ├── router.py #     HTTP endpoints (thin; mounted at root)
        ├── service.py#     business logic (no FastAPI imports)
        └── schemas.py#     request/response models
```

### Anatomy of a module

A module contains only the layers it needs. The full vocabulary:

```
modules/<feature>/
├── __init__.py       # re-exports the module's `router`
├── router.py         # HTTP endpoints — thin, delegate to service
├── service.py        # business logic — framework-agnostic, reusable
├── schemas.py        # Pydantic request/response models (the API contract)
├── models.py         # persistence/domain models           (as needed)
├── dependencies.py   # module-specific FastAPI dependencies (as needed)
└── exceptions.py     # module-specific errors               (as needed)
```

### Adding a module

1. Create `modules/<feature>/` with at least `router.py`, `service.py`,
   `schemas.py`, and an `__init__.py` that re-exports `router`.
2. Register it in `router.py`:

   ```python
   from api.modules.<feature> import router as <feature>_router

   api_router.include_router(<feature>_router, prefix="/<feature>", tags=["<feature>"])
   ```

   It is now served under `/api/v1/<feature>`.

### Rules of thumb

- **routers** translate HTTP <-> Python and delegate to **services**. Keep them thin.
- **services** hold business logic. No FastAPI imports — so they stay unit-testable
  and reusable (e.g. by the worker).
- **schemas** define the external contract. Keep separate from any DB/domain models.
- **core** holds only what every module shares; anything feature-specific belongs in
  the module.

## Tests

```bash
uv run pytest apps/api
```
