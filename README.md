# Yellow River GeoAgent

面向黄河流域场景的地图智能体底座。

## 目标

- 支持黄河流域专题地图查询
- 支持地理空间数据接入与统一抽象
- 支持大模型和工具调用式 Agent 编排
- 支持未来扩展为 Web 地图、API 服务和批处理任务

## 设计原则

- 分层清晰，领域逻辑与基础设施解耦
- 先定义接口，再接具体实现
- 面向扩展，便于后续接入高德、天地图、PostGIS、GeoServer、向量库和 LLM

## 推荐架构

- `domain`: 业务领域模型与核心规则
- `services`: 面向用例的应用服务
- `infrastructure`: 外部系统适配层
- `api`: 对外 HTTP 接口
- `core`: 配置、日志、异常等公共基础能力

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
uvicorn yellow_river_geoagent.main:app --reload
```

启动后访问：

- `GET /health`
- `GET /api/v1/map/capabilities`
- `POST /api/v1/agent/query`

