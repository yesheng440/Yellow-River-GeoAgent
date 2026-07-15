from fastapi.testclient import TestClient

from yellow_river_geoagent.main import app


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agent_query_endpoint() -> None:
    client = TestClient(app)
    response = client.post("/api/v1/agent/query", json={"question": "黄河流域哪里有重要湿地？"})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] in {"map_search", "data_qa"}
    assert "answer" in body

