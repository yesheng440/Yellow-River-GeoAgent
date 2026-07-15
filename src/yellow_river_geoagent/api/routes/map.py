from fastapi import APIRouter

from yellow_river_geoagent.domain.schemas import CapabilityResponse
from yellow_river_geoagent.services.map_service import MapService

router = APIRouter(prefix="/map", tags=["map"])


@router.get("/capabilities", response_model=CapabilityResponse)
def capabilities() -> CapabilityResponse:
    service = MapService()
    data = service.capabilities()
    return CapabilityResponse(
        providers=data["providers"],
        features=data["features"],
    )

