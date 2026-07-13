from typing import Any


class GeoDataSource:
    def search_layers(self, keyword: str) -> list[dict[str, Any]]:
        return [{"name": f"mock:{keyword}", "type": "vector", "source": "mock"}]

