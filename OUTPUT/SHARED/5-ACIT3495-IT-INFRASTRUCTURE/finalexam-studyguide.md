# ACIT3495 — Final Exam Study Guide
> ~90 min | Closed Book (assumed) | Written MC + T/F | Thu Apr 24, 2026 @ 15:30

---

## 1. Docker vs Kubernetes — Core Distinction

| Tool | Role |
|------|------|
| **Docker** | Container platform (build, run, ship containers) |
| **Kubernetes** | Orchestration tool (automates deployment, scaling, management of containers) |

**Docker is NOT an orchestration tool.** Kubernetes is the orchestration tool.

---

## 2. Docker — Commands

| Command | Action |
|---------|--------|
| `docker run` | Create AND start a container from an image |
| `docker pull` | Download image from registry (does NOT run it) |
| `docker exec` | Connect to / run command in a **running** container |
| `docker stop` | Stop a running container |
| `docker rm` | Remove a **container** |
| `docker rmi` | Remove an **image** |
| `docker build` | Build image from Dockerfile |
| `docker images` | List local images |
| `docker ps` | List running containers |
| `docker network create` | Create a Docker network |

**⚠️ Exam Traps:**
- `docker run` ≠ `docker pull` — run CREATES and STARTS; pull only DOWNLOADS
- `docker rm` ≠ `docker rmi` — rm removes CONTAINERS; rmi removes IMAGES
- `docker exec` = connects to RUNNING container (not `docker run`, which creates a new one)

---

## 3. Docker — Core Concepts

**Docker Volume:**
- Purpose: **persist data even after container is deleted**
- NOT just for bind mounting directories (that's one use case, not the purpose)

**Dockerfile:**
- Stores Docker **build instructions** (not: creates images directly, not: packages single files)

**Port Mapping (`-p`):**
- Exposes container port to host: `docker run -p 8080:80 nginx`

**Restart Policy:**
- Controls behavior when container exits
- `--restart always` = restart container when it exits (or on Docker restart)

**Image vs Container:**
- **Image** = blueprint (template, read-only)
- **Container** = runtime instance (running from an image)

**Docker Compose:**
- Manages **multi-container** applications using a `docker-compose.yml` file

---

## 4. Kubernetes — Core Concepts

**Pod:**
- Smallest deployable unit in Kubernetes
- Can contain one or more containers
- Containers in the same pod share: **network namespace** + storage
- Containers in same pod communicate via **localhost**

**Deployment:**
- Manages desired state for a set of Pods
- Ensures specified number of replicas running
- Facilitates **rolling updates and rollbacks**

**ReplicaSet:**
- Directly ensures a specified number of identical pod replicas
- Automatically replaces failed pods
- Usually managed by a Deployment (not created directly)

**Labels:**
- Key-value pairs attached to K8s objects
- Used to **logically group and select** related objects (Pods, Deployments, Services)

**Namespaces:**
- Virtual clusters within a K8s cluster for resource isolation

---

## 5. Kubernetes — Service Types

| Type | Access | Notes |
|------|--------|-------|
| **ClusterIP** | Internal only | **Default** service type; only reachable within cluster |
| **NodePort** | External (via node) | Exposes on static port **30000–32767** on each node |
| **LoadBalancer** | External (cloud) | Provisions **external load balancer** from cloud provider |
| **ExternalName** | DNS mapping | Maps service to external DNS name |
| **Headless** | No cluster IP | Direct Pod IP resolution |

**⚠️ Exam Traps:**
- ClusterIP = DEFAULT type (NOT NodePort, NOT LoadBalancer)
- LoadBalancer = needs a cloud provider to provision external LB
- NodePort range = exactly **30000–32767**
- `kube-apiserver` = exposes the Kubernetes API (NOT manages network policies)

---

## 6. Kubernetes — Cluster Components

| Component | Role |
|-----------|------|
| **kube-apiserver** | Exposes the Kubernetes API (front-end of control plane) |
| **etcd** | Backing store for all cluster data |
| **kube-scheduler** | Assigns Pods to Nodes |
| **kubelet** | Agent on each node; ensures containers run in Pods |
| **kube-proxy** | Maintains network rules on nodes |

**Docker Desktop K8s:**
- Lightweight **single-node** Kubernetes cluster
- Integrated directly within Docker Desktop
- NOT production-grade; NOT multi-master; does NOT require cloud account

**AWS managed Kubernetes = EKS** (Elastic Kubernetes Service)
- Google = GKE, Azure = AKS, DigitalOcean = DOKS

---

## 7. Kubernetes — State Persistence

**PersistentVolume (PV):**
- Cluster-level storage resource provisioned by admin
- `capacity` field = how much storage is available
- `accessModes` field = how the volume can be accessed

**PersistentVolumeClaim (PVC):**
- Request for storage from available PVs
- Purpose: allow Pods to claim storage resources
- NOT for: exposing Pods, backing up images, creating nodes, defining replicas

**Key rule:** Data on a properly mounted PV **persists independently of the Pod lifecycle** — deleting/recreating the Pod does NOT delete PV data.

**Common pattern:** Deployment (web app) + PVC (persistent storage) + LoadBalancer Service (external access)

---

## 8. Kubernetes — Update Strategies

| Strategy | Description |
|----------|-------------|
| **RollingUpdate** | Gradually replaces old Pods with new ones — **minimal downtime** |
| **Recreate** | Terminates all old Pods before creating new ones — downtime occurs |

**RollingUpdate** = most common, default for Deployments.

---

## 9. Kubernetes — initContainers & Sidecar

**initContainer:**
- Runs **before** the main application container starts
- Use case: pre-populate a shared volume with config/data before app starts
- Runs to completion, then main container starts

**Sidecar container:**
- Runs **alongside** the main container in the same Pod
- Use case: log collection, proxy, monitoring

**Pattern (exam):** Deployment with initContainer writing setup files to shared volume → expose with ClusterIP Service (internal access)

---

## 10. Kubernetes — ConfigMaps & Secrets

| Object | Purpose | Sensitivity |
|--------|---------|------------|
| **ConfigMap** | Store non-sensitive config as key-value pairs | Not sensitive |
| **Secret** | Store sensitive data (passwords, API keys, tokens) | Sensitive; base64-encoded |

**ConfigMap creation:**
```
kubectl create configmap config1 --from-literal=sleep-interval=25
```

**Secret creation:**
```
kubectl create secret generic my-secret --from-literal=pwd=password
```

Secrets are stored **base64-encoded** (NOT encrypted by default in K8s).

---

## 11. Key kubectl Commands

| Command | Purpose |
|---------|---------|
| `kubectl get pods` | List pods |
| `kubectl get svc` | List services |
| `kubectl get deployments` | List deployments |
| `kubectl get replicaset` | List replica sets |
| `kubectl get pv` / `kubectl get pvc` | List PVs / PVCs |
| `kubectl describe pods` | Detailed pod info |
| `kubectl exec <pod> -it -- /bin/sh` | Shell into pod |
| `kubectl scale deployment app1 --replicas 3` | Scale deployment |
| `kubectl get configmaps` | List ConfigMaps |
| `kubectl get secrets` | List Secrets |

---

## 12. Quick-Fire True/False Traps

| Statement | Answer |
|-----------|--------|
| Docker is an orchestration tool | **FALSE** — Kubernetes is |
| `docker run` creates AND starts a container | **TRUE** |
| `docker pull` creates and starts a container | **FALSE** — only downloads the image |
| `docker exec` connects to a running container | **TRUE** |
| `docker rm` removes a Docker image | **FALSE** — `docker rmi` removes images; `docker rm` removes containers |
| Docker volume = bind mount a directory | **FALSE** — volume purpose is to persist data after container deletion |
| Pod = smallest deployable unit in K8s | **TRUE** |
| Containers in same Pod share network namespace | **TRUE** |
| ClusterIP is the default Service type in K8s | **TRUE** |
| LoadBalancer Service works without a cloud provider | **FALSE** — requires cloud provider to provision LB |
| NodePort range is 30000–32767 | **TRUE** |
| kube-apiserver manages K8s network policies | **FALSE** — it exposes the K8s API |
| ReplicaSet creates the initial Pod deployment template | **FALSE** — Deployment manages that; ReplicaSet ensures replica count |
| PVC = Persistent Volume Claim requests storage from PVs | **TRUE** |
| Deleting a Pod also deletes data on its PersistentVolume | **FALSE** — PV data persists independently |
| `capacity` field in PV spec = amount of storage available | **TRUE** |
| RollingUpdate causes downtime during deployment | **FALSE** — minimal downtime |
| Docker Desktop K8s = multi-node production cluster | **FALSE** — single-node, lightweight |
| EKS = AWS managed Kubernetes service | **TRUE** |
| ConfigMap stores sensitive data like passwords | **FALSE** — Secrets store sensitive data; ConfigMap for non-sensitive config |
| Secrets are encrypted by default in Kubernetes | **FALSE** — stored base64-encoded (not encrypted) |
| initContainer runs after the main container starts | **FALSE** — runs BEFORE main container |
