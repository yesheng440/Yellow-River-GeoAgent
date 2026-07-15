from fastapi import FastAPI

from yellow_river_geoagent.api.routes.health import router as health_router
from yellow_river_geoagent.api.routes.agent import router as agent_router
from yellow_river_geoagent.api.routes.map import router as map_router
from yellow_river_geoagent.core.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Yellow River basin map intelligence agent",
    )
    app.include_router(health_router)
    app.include_router(agent_router, prefix="/api/v1")
    app.include_router(map_router, prefix="/api/v1")
    return app


app = create_app()

