"""Feature modules.

Each module is a self-contained vertical slice of one capability and owns every
layer it needs:

    modules/<feature>/
    ├── __init__.py        # re-exports the module's `router`
    ├── router.py          # HTTP endpoints (thin; delegate to service)
    ├── service.py         # business logic (no FastAPI imports)
    ├── schemas.py         # request/response models (the API contract)
    ├── models.py          # persistence/domain models           (as needed)
    ├── dependencies.py    # module-specific FastAPI dependencies (as needed)
    └── exceptions.py      # module-specific errors               (as needed)

Cross-cutting concerns shared by all modules live in ``api.core``. Feature
modules are registered for the versioned API in ``api.router``.
"""
