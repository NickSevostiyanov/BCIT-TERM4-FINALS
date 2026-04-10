# ACIT3855 — Final Exam Study Guide
> 180 min | Open Book | Paper notes/cheatsheets ONLY — no electronics | DTC 825 | April 20 @ 2:30 PM
> **Format: MC + short answers + implement simple API + fill YAML blanks + write Python app.py code**
> **Bring this printed + the cheatsheet. This is the concepts layer.**

---

## 1. Microservices vs Monolith (Martin Fowler)

### Benefits of Microservices
- **Technology Diversity** — mix languages, frameworks, databases per service (polyglot)
- **Strong Module Boundaries** — enforces modular structure, important for large teams
- **Independent Deployment** — deploy/redeploy one service without touching others
- **Scalability** — scale only the services that need it

### Costs of Microservices
- **Eventual Consistency** — distributed data = no cross-service DB transactions; everyone must handle it
- **Operational Complexity** — need mature ops team to manage many services
- **Distribution** — remote calls are slow and can fail; harder to program than in-process calls

### Key Terms
- **Polyglot** — each service can use different language/framework/database
- **Conway's Law** — organization's system design mirrors its communication structure
  - Teams organized by technology layers (UI/DB/Middleware) → time-consuming approval process
  - Microservices teams organized by **business capability** instead
- **CI/CD** — NOT exclusive to microservices; also applies to monoliths

---

## 2. REST API & Connexion

### HTTP Methods
| Method | Purpose |
|--------|---------|
| GET | Retrieve resource |
| POST | Create resource |
| PUT | Update/replace resource |
| DELETE | Remove resource |

### Connexion + OpenAPI
- API defined in a YAML file (OpenAPI 3.0 spec)
- **`operationId`** — routes an endpoint to a specific Python function
- **`strict_validation=True`** — enables automatic validation of request parameters against spec
- **`validate_responses=True`** — validates responses (optional, separate flag)

### apscheduler
```python
from apscheduler.schedulers.background import BackgroundScheduler

def populate_stats():
    """ runs periodically """
    ...

def init_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(populate_stats, 'interval',
                  seconds=app_config['scheduler']['period_sec'])
    sched.start()
```
- Runs scheduled job in background daemon thread
- Period stored in external config file (not hardcoded)
- Both the API (Connexion) and scheduler run in the same application

---

## 3. OpenAPI 3.0 Specification

### Structure
```yaml
openapi: "3.0.0"
info:         # Meta information
  title: My API
  version: "1.0"
  description: ...

paths:        # Endpoint definitions
  /artists:
    get:
      operationId: app.get_artists
      parameters:
        - name: limit
          in: query        # query | path | header | cookie
          required: false
          schema:
            type: integer
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Artist'
        '400':
          description: Invalid request

components:   # Reusable definitions
  schemas:
    Artist:
      type: object
      required:
        - username
      properties:
        artist_name:
          type: string
        username:
          type: string
```

### Key Concepts
- **Metadata** keywords: `title`, `version`, `description`, `contact`, `security`
- **Path Items** include: `parameters`, `responses`, `request bodies`, `operation verbs`
- **Components** — for REUSE: `schemas`, `parameters`, `responses`, `requestBodies`
- **Why components?** → Reuse — define once, reference with `$ref`
- **YAML preferred** over JSON (easier to read/write)
- **`in: query`** — use query params to limit amount of data returned (e.g., `?limit=5&offset=10`)

---

## 4. Data Persistence

### Polyglot Persistence
- Each service manages its OWN database (private)
- Accessible ONLY via its API — not direct DB access by other services
- Services transactions only involve THEIR OWN database (NOT a central one)
- A monolith CAN use polyglot persistence, but it's less common

### Database Per Service Pattern
**Valid SQL options:**
- Private-tables-per-service
- Schema-per-service
- Database-server-per-service

**Benefits:**
- Each service can use the DB best suited to its needs
- Services are **loosely coupled** → developed/deployed/scaled independently

**Drawbacks:**
- Complex to manage multiple DBs
- Transactions spanning multiple services are NOT straightforward
- Queries joining data across services are challenging
- Does NOT help ensure tight coupling (this is a drawback, not a benefit)

### SQLite vs MySQL
| SQLite | MySQL |
|--------|-------|
| Serverless, self-contained | Requires a server |
| Runs embedded in application | Client-server architecture over network |
| Good for dev/testing | Good for production |

### SQLAlchemy
- **Declarative model** — Python class that maps to a DB table
- `all_readings` returned from `session.query(...).all()` → **List** (not object/string/dict)

---

## 5. Logging & Tracing

### Event Logging vs Software Tracing
| | Event Logging | Software Tracing |
|--|---------------|-----------------|
| **Audience** | System Administrators | Developers |
| **Level** | High-level info (e.g. failed install) | Low-level info (debug detail) |
| **Noise** | Must NOT be noisy | CAN be noisy |
| **Purpose** | Diagnostics and auditing | Debugging |

### Python Logging Module
- 5 standard levels (in order): **DEBUG, INFO, WARNING, ERROR, CRITICAL**
- `level` in config = **minimum** severity logged (not maximum)
- Configuration methods:
  1. `basicConfig`
  2. Default Root Logger
  3. External configuration file (`log_conf.yml`)
- Tracing is used by **developers** for debugging (NOT system admins)

### Externalized Configuration
- Config in `app_conf.yml` — values like DB credentials, 3rd party URLs, scheduler period
- **Pattern goal:** service runs in multiple environments (dev/test/staging/prod) WITHOUT modification
  - ⚠️ Current limitation: rebuilding Docker images IS required if `app_conf.yml` changes
- Example from external config: Database credentials, 3rd Party Service URLs

### Log Aggregation
- In microservices: each service generates logs in its Docker container
- Centralized logging service aggregates logs from all instances
- Problem: handling a **large volume** of log messages
- View logs via: `docker logs <container_id>`, `docker-compose logs`, running container in foreground (no `-d`)

---

## 6. Messaging & Kafka

### REST/HTTP vs Messaging
| REST/HTTP | Messaging |
|-----------|-----------|
| **Synchronous** | **Asynchronous** |
| Request/reply | Fire-and-forget |
| Scales poorly for multi-broadcast | Scales well |
| Good for: SOA, public APIs, request/reply | Good for: events, multi-consumer, async |

**Why REST doesn't scale for microservices:**
- Cannot simultaneously deliver event to multiple places
- Cannot deliver messages asynchronously
- Doesn't scale as more applications/instances added

### Kafka
- Open-source stream processing platform
- **Features:** Low-latency, High-throughput, Distributed, Massively Scalable
- **Use cases:** Activity Monitoring, Log Aggregation, Messaging, Database
- **Topic** = stream of records/messages in key-value format; each assigned an **offset** (sequence number)
- **Producers** — publish messages to topics
- **Consumers** — subscribe to topics and read messages
- **Broker** = instance of Kafka responsible for message exchange
- Kafka can be deployed as a **cluster** for high-availability (NOT single machine only)
- Advantages of messaging: **Scalability, High-Availability, Producer/Consumer Decoupling, Pub/Sub Pattern**

### Kafka Error Handling
- **Producer** exceptions to handle for connection loss: `LeaderNotAvailable`, `SocketDisconnectedError`
- **Consumer** exception to handle: `SocketDisconnectedError`
- On connection loss: **restart** the consumer/producer object to re-establish connection

---

## 7. Docker

### Core Concepts
- **Image** = blueprint; **Container** = running instance of an image
- Container filesystem (not in volume/bind mount) is **deleted when container is removed** (NOT when stopped)
- **Volume** — completely managed by Docker; persists after container removed
  - Volume is NOT automatically removed when container is removed (separate step needed)
  - Volume IS automatically created if it doesn't exist when container starts
- **Bind mount** — mounts a file/directory from the Host VM
- **tmpfs mount** — stores data in memory on Host VM (not persisted)
- Three mount types: `volume`, `bind`, `tmpfs`

### Docker Compose
- `docker-compose up -d` — start in background
- `docker-compose up --scale service=3` — start 3 replicas of a service
- `docker-compose logs` — view aggregated logs

### Externalized Config (Docker)
- Current state: must rebuild image when `app_conf.yml` changes (not true externalized config yet)
- True externalized config = service runs in any environment WITHOUT rebuilding

---

## 8. Same Origin Policy (SOP) & CORS

### Same Origin Policy
- Browser security feature
- Prevents a web page from making requests to a **different origin** than the one it was served from
- Origin = scheme (http/https) + host + port
- Only applies to **browser-initiated requests** (not server-to-server)

### CORS (Cross-Origin Resource Sharing)
- Mechanism to **relax SOP** when cross-origin requests are needed
- Server adds headers to allow specific origins/methods
- **Preflight request** — browser sends OPTIONS request first for non-simple requests
- Key headers:
  - `Access-Control-Allow-Origin`
  - `Access-Control-Allow-Methods`
  - `Access-Control-Allow-Headers`

---

## 9. Deployment Strategies

| Strategy | Description | High-Availability? |
|----------|-------------|:-----------------:|
| **Recreate** | Stop all old instances, then start new ones | ❌ No (downtime) |
| **Ramped (Rolling)** | Gradually replace old with new | ✅ Yes |
| **Blue/Green** | Run old (green) + new (blue) in parallel; switch traffic | ✅ Yes (easy rollback) |
| **Canary** | Route small % of traffic to new version; test with real users | ✅ Yes |

- **Blue/Green:** Blue = NEW version, Green = EXISTING/old version (common trick: statement says opposite)
- **Canary:** Tested by **End Users** in production (not developers/testers)
- **Docker Compose** provides: **Recreate** strategy (not blue/green, not canary)
- **Recreate in Kubernetes** is NOT high-availability (service goes down during update)

---

## 10. Load Balancing (NGINX)

- NGINX = **software** load balancer (NOT hardware)
- **Default strategy: Round Robin** — requests distributed sequentially across server group
- Other strategies:
  - **Least Connected** — send to server with fewest current connections
  - **IP Hash** — client IP determines which server receives request
  - **Random with Two Choices** — picks two at random, uses least connections
  - **Hash** — user-defined hash
- Load balancer provides: **Availability** (redirect if server down) + **Scalability** (add/remove servers)
- Three primary functions: distribute traffic, send only to online servers, allow adding/removing servers

---

## 11. Testing Types

Automated testing segments in microservices:
- **Unit Testing** — individual functions/classes
- **Integration Testing** — interactions between components
- **UI Functional Testing** — browser-level tests
- **End-to-End Testing** — full system flow

Logging best practices in microservices:
1. **Searchable logs**
2. **Invest in a logging framework** (don't build your own)
3. **Easily changeable log levels**

### Distributed Tracing
- Tracks a single request as it flows through multiple services
- Example: observe event as it's received by Receiver → stored by Storage → processed by Processing
- Advantages: end-to-end visibility, faster for developers to trace issues

### Technical Debt
- The implied cost of additional rework caused by choosing a quick/easy solution now
- Represented as software issues (bugs or improvement items)

---

## 12. Quick-Fire Exam Facts

| Statement | Answer |
|-----------|--------|
| Independent Deployment is a COST of microservices | **FALSE** — it's a BENEFIT |
| Eventual Consistency is a COST of microservices | **TRUE** |
| CI/CD can only be applied to microservices | **FALSE** |
| Polyglot = each service uses different language/DB | **TRUE** |
| Monolith CANNOT use Polyglot Persistence | **FALSE** — it can, just less common |
| Service transactions use a central database | **FALSE** — only their own DB |
| `strict_validation=True` validates request params | **TRUE** |
| OpenAPI specs are best written in JSON | **FALSE** — YAML is recommended |
| Kafka can only run on a single machine | **FALSE** — runs as cluster |
| Messaging is asynchronous communication | **TRUE** |
| REST/HTTP is asynchronous communication | **FALSE** — synchronous |
| Volume is deleted when container is removed | **FALSE** — separate step required |
| Volume is auto-created if missing | **TRUE** |
| Data in container filesystem persists after remove | **FALSE** — deleted |
| Blue = OLD version in blue/green deployment | **FALSE** — Blue = NEW |
| Canary tests with End Users in production | **TRUE** |
| Docker Compose provides Blue/Green strategy | **FALSE** — Recreate |
| NGINX is a hardware load balancer | **FALSE** — software |
| NGINX default = Round Robin | **TRUE** |
| Receiver→Storage→Processing = Distributed Tracing | **TRUE** |
| `level` = minimum severity logged | **TRUE** |
| Tracing is for system administrators | **FALSE** — developers |
| 5 logging levels = DEBUG/INFO/WARNING/ERROR/CRITICAL | **TRUE** |

---

## 13. Code to Know (Exam has "implement simple API" + "fill YAML blanks" + write app.py)

### Minimal app.py (Connexion)
```python
import connexion

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('openapi.yaml', strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080, use_reloader=False)
```

### Minimal OpenAPI endpoint
```yaml
openapi: "3.0.0"
info:
  title: My Service
  version: "1.0"
paths:
  /readings:
    post:
      operationId: app.post_reading
      summary: Store a reading
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Reading'
      responses:
        '201':
          description: Reading stored
        '400':
          description: Bad request
components:
  schemas:
    Reading:
      type: object
      required:
        - sensor_id
        - value
      properties:
        sensor_id:
          type: string
        value:
          type: number
```

### SQLAlchemy model (declarative)
```python
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'readings'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String(36), nullable=False)
    value = Column(Integer, nullable=False)
```

### Kafka producer (Python)
```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='kafka:9092')
msg = {"sensor_id": "abc", "value": 42}
producer.send('events', json.dumps(msg).encode('utf-8'))
producer.flush()
```

### app_conf.yml (externalized config)
```yaml
datastore:
  user: root
  password: mypassword
  hostname: db
  port: 3306
  db: readings

scheduler:
  period_sec: 5

kafka:
  hostname: kafka
  port: 9092
  topic: events
```
