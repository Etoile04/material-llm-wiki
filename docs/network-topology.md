# 网络拓扑与端口配置

> **维护规则：** 容器配置变更时只改此文件，不改技能文件。技能文件引用此文件。
> **最后更新：** 2026-05-30

## 主机

| 主机 | 系统 | Tailscale IP | SSH |
|------|------|-------------|-----|
| Mac Studio (本地) | macOS 15.5 arm64 | — | — |
| ThinkStation P3 Tower | Ubuntu 22.04 x86_64 | 100.70.30.21 | `ssh z203@100.70.30.21` |

---

## ThinkStation Docker 容器端口映射

### 核心业务服务

| 容器名 | 服务 | 映射端口 | 数据库/路径 | 说明 |
|--------|------|---------|------------|------|
| nucpot-nucpot-db-1 | PostgreSQL 16 | **5432** | 库: `nucpot`, 用户: `nucpot` | 势函数验证：reference_values / potentials / verifications |
| nfmd-postgres | PostgreSQL 16 | **15432** | 库: `nfmd`, 用户: `postgres` | NFMD 材料数据库：parameters / materials / literature / categories |
| nucpot-autovc-api-1 | FastAPI | **8001** | `/api/references` | 势函数验证 REST API |
| autovc-redis | Redis 7 | **6379** | — | 验证任务队列 |

### NFMD 操作速查

```bash
# SSH 到 ThinkStation 后
docker exec nfmd-postgres psql -U postgres -d nfmd -c "SQL"
# 从 Mac 远程直连 PG
psql -h 100.70.30.21 -p 15432 -U postgres -d nfmd
# 备份
docker exec nfmd-postgres pg_dump -U postgres -d nfmd --format=custom > backup.dump
```

### nucpot 操作速查

```bash
docker exec nucpot-nucpot-db-1 psql -U nucpot -d nucpot -c "SQL"
# 验证 API
curl http://100.70.30.21:8001/api/references
```

### TrustGraph (知识图谱)

| 端口 | 服务 |
|------|------|
| 8000 | MCP Server |
| 8088 | API Gateway |
| 8888 | Workbench UI |
| 9870 | DDG MCP Server |
| 6333-6334 | Qdrant 向量库 |
| 7474 / 7687 | Neo4j 图数据库 |
| 9042 | Cassandra |
| 6650 / 8080 | Pulsar 消息 |
| 2181 / 2888 / 3888 | Zookeeper |
| 3900-3904 | Garage 对象存储 |
| 3000 | Grafana 监控 |
| 3100 | Loki 日志 |

### 其他服务

| 容器名 | 端口 | 服务 |
|--------|------|------|
| release-openspg-server | **8887** | OpenSPG 知识图谱 |
| release-openspg-mysql | **3306** | MySQL (OpenSPG 后端) |
| release-openspg-minio | **9000-9001** | MinIO 对象存储 |
| nb-docker-app | **13000** | NocoBase 低代码平台 |

---

## Mac 本地服务

| 端口 | 进程 | 说明 |
|------|------|------|
| 8000 | python3 (MinerU) | PDF 解析服务 |
| 19001 | node (OpenClaw) | Gateway |
| 19003 | node (OpenClaw) | Browser control |
| 18810-18817 | node (OpenClaw) | Internal runtime |

---

## 变更记录

| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-05-30 | nfmd-postgres 端口 5432 → 15432 | 与 nucpot-nucpot-db-1 端口冲突，容器无法启动 |
