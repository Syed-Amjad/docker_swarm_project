# Docker Swarm Microservices Monitoring Project

A complete DevOps showcase project demonstrating **Docker Swarm orchestration**, **microservices architecture**, **metrics collection**, and **monitoring** using Prometheus and Grafana, deployed on an **AWS EC2** instance.

---

## 🚀 Project Overview

This project simulates a production-grade containerized application environment consisting of:

### 🧱 Services Included:

* **Python Flask App (3 replicas)**
* **Redis** (caching)
* **PostgreSQL** (database)
* **Nginx** (as reverse proxy)
* **Prometheus** (metrics collection)
* **Grafana** (metrics visualization)
* **Portainer** (Docker management GUI)
* **cAdvisor** (Docker container monitoring)

## 📁 Folder Structure

```
docker-swarm-showcase/
├── app/                  # Flask App
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
├── nginx/                # Nginx reverse proxy
│   ├── Dockerfile
│   └── nginx.conf
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── provisioning/
│       ├── dashboards/
│       └── datasources/
├── docker-compose.yml
├── docker-stack.yml
├── .env
├── deploy-swarm.sh
└── README.md
```

---

## ⚙️ Tech Stack

| Category         | Tools                                |
| ---------------- | ------------------------------------ |
| Containerization | Docker, Docker Compose, Docker Swarm |
| Reverse Proxy    | Nginx                                |
| Monitoring       | Prometheus, Grafana, cAdvisor        |
| Database         | PostgreSQL                           |
| Cache            | Redis                                |
| Deployment       | AWS EC2 (Ubuntu 22.04 LTS via WSL2)  |
| Dashboard        | Portainer                            |

---

## 🧪 Setup & Deployment

### 🔐 1. Clone and Configure

```bash
git clone https://github.com/Syed-Amjad/docker_swarm_project
cd docker-swarm-project
```

Create a `.env` file:

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
```

---

### 🐳 2. Build Required Images

```bash
docker build -t flask-app ./app
docker build -t nginx-proxy ./nginx
```

---

### 🌐 3. Initialize Docker Swarm (if not done already)

```bash
sudo docker swarm init
```

---

### 🚀 4. Deploy Stack

```bash
docker stack deploy -c docker-stack.yml mystack
```

---

## 🔍 Ports & Access

| Service               | Port | URL                    |
| --------------------- | ---- | ---------------------- |
| Flask App (via Nginx) | 8082 | http\://<EC2-IP>:8082  |
| Prometheus            | 9090 | http\://<EC2-IP>:9090  |
| Grafana               | 3000 | http\://<EC2-IP>:3000  |
| Portainer             | 9443 | https\://<EC2-IP>:9443 |
| cAdvisor              | 8080 | http\://<EC2-IP>:8080  |

---

## 📊 Metrics Integration

* **Prometheus config** targets Flask app at `/metrics` and cAdvisor on port 8080.
* **Flask app** uses `prometheus_flask_exporter`.
* **Grafana** uses dashboard ID `193` for Docker monitoring.

Prometheus config snippet:

```yaml
- job_name: 'flaskapp'
  static_configs:
    - targets: ['app:8082']

- job_name: 'cadvisor'
  static_configs:
    - targets: ['cadvisor:8080']
```

---

## 🐛 Troubleshooting Highlights

* **Nginx container failed** due to old cache — resolved by rebuilding and restarting via Portainer.
* **Prometheus error** due to incorrect `Content-Type` — resolved by switching to `prometheus_flask_exporter`.
* **Stack stuck in old state** — resolved with `docker stack rm mystack` and clean redeployment.

---


## 🤝 License & Contact

Open for contributions and collaboration. DM me on [LinkedIn](https://www.linkedin.com/in/syed-amjad-ali-4188002a0/) or GitHub.

---

✅ **Completed by:** Syed Amjad Ali
🔗 Project: [github.com/Syed-Amjad/docker-swarm-project]((https://github.com/Syed-Amjad/docker_swarm_project))

---

> "Building systems is easy. Running them reliably at scale is the real engineering challenge."
