from pydantic import BaseModel, Field


class AgentQueryRequest(BaseModel):
    question: str = Field(min_length=1, description="用户的地图问题")


class LayerItem(BaseModel):
    name: str
    type: str
    source: str | None = None


class AgentQueryResponse(BaseModel):
    answer: str
    intent: str
    layers: list[LayerItem] = Field(default_factory=list)


class CapabilityResponse(BaseModel):
    providers: dict[str, str]
    features: list[str]
