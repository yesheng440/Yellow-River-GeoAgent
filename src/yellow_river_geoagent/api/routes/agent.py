from fastapi import APIRouter

from yellow_river_geoagent.domain.schemas import AgentQueryRequest, AgentQueryResponse
from yellow_river_geoagent.services.agent_service import AgentService

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/query", response_model=AgentQueryResponse)
def query(payload: AgentQueryRequest) -> AgentQueryResponse:
    service = AgentService()
    return service.answer(payload.question)

