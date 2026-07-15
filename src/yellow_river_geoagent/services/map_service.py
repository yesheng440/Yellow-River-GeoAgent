from yellow_river_geoagent.domain.models import MapTask, MapResult, QueryIntent


class MapService:
    def capabilities(self) -> dict[str, object]:
        return {
            "providers": {
                "map": "mock",
                "llm": "mock",
            },
            "features": [
                "intent_recognition",
                "layer_composition",
                "spatial_reasoning",
                "route_planning",
            ],
        }

    def build_task(self, question: str) -> MapTask:
        intent = self._infer_intent(question)
        return MapTask(question=question, intent=intent)

    def execute(self, task: MapTask) -> MapResult:
        if task.intent == QueryIntent.MAP_SEARCH:
            return MapResult(
                answer=f"已为问题生成地图检索任务：{task.question}",
                layers=[{"name": "黄河流域基础图层", "type": "vector", "source": "mock"}],
            )
        if task.intent == QueryIntent.SPATIAL_ANALYSIS:
            return MapResult(
                answer=f"已为问题生成空间分析任务：{task.question}",
                layers=[{"name": "分析图层", "type": "analysis", "source": "mock"}],
            )
        if task.intent == QueryIntent.ROUTE_PLANNING:
            return MapResult(
                answer=f"已为问题生成路径规划任务：{task.question}",
                layers=[{"name": "路径图层", "type": "route", "source": "mock"}],
            )
        return MapResult(answer=f"已为问题生成数据问答任务：{task.question}")

    def _infer_intent(self, question: str) -> QueryIntent:
        text = question.lower()
        if any(keyword in text for keyword in ("路线", "路径", "route", "导航")):
            return QueryIntent.ROUTE_PLANNING
        if any(keyword in text for keyword in ("分析", "空间", "buffer", "叠加", "统计")):
            return QueryIntent.SPATIAL_ANALYSIS
        if any(keyword in text for keyword in ("哪里", "位置", "查询", "查找", "map", "图层")):
            return QueryIntent.MAP_SEARCH
        return QueryIntent.DATA_QA

