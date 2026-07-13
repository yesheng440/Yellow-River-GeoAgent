from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class QueryIntent(str, Enum):
    MAP_SEARCH = "map_search"
    SPATIAL_ANALYSIS = "spatial_analysis"
    ROUTE_PLANNING = "route_planning"
    DATA_QA = "data_qa"


@dataclass(slots=True)
class MapTask:
    question: str
    intent: QueryIntent
    context: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MapResult:
    answer: str
    layers: list[dict[str, Any]] = field(default_factory=list)
    artifacts: list[dict[str, Any]] = field(default_factory=list)

