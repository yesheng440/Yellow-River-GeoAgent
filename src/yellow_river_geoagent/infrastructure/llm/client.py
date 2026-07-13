from yellow_river_geoagent.core.errors import CapabilityError


class LLMClient:
    def generate(self, prompt: str) -> str:
        raise CapabilityError("LLM provider is not configured yet")

