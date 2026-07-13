from yellow_river_geoagent.domain.models import MapResult
from yellow_river_geoagent.domain.schemas import AgentQueryResponse
from yellow_river_geoagent.services.map_service import MapService


class AgentService:
    def __init__(self, map_service: MapService | None = None) -> None:
        self._map_service = map_service or MapService()

    def answer(self, question: str) -> AgentQueryResponse:
        task = self._map_service.build_task(question)
        result: MapResult = self._map_service.execute(task)
        return AgentQueryResponse(
            answer=result.answer,
            intent=task.intent.value,
            layers=[{"name": item["name"], "type": item["type"], "source": item.get("source")} for item in result.layers],
        )

