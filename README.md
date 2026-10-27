# ?? Incident Management System (DevOps Project 8)

A lightweight automated incident management and alerting engine built with **Flask**, **Docker**, and **Python**, featuring real-time system monitoring, webhook-driven incident tracking, and a modern dark-mode dashboard UI.

---

## ?? Features
- **Real-Time System Monitoring:** Tracks system operational status and active open incidents dynamically.
- **Webhook Alert Engine (\/alert\):** Accepts automated system alerts and logs incidents instantly with severity levels (\CRITICAL\, \HIGH\, \MEDIUM\).
- **Interactive UI Dashboard:** Built-in web interface with a "+ Trigger Test Incident" button to simulate and monitor incidents in real-time.
- **Dockerized Architecture:** Containerized using Docker for consistent, cross-platform deployment.

---

## ??? Tech Stack
- **Backend:** Python, Flask
- **Containerization:** Docker
- **Frontend:** HTML5, CSS3 (Embedded Responsive Dashboard)

---

## ?? Quick Start & Installation

### 1. Clone the Repository
\\\ash
git clone https://github.com/vimalvajpeyi08-arch/devops-project-8.git
cd devops-project-8
\\\

### 2. Build the Docker Image
\\\ash
docker build -t devops-project-8 .
\\\

### 3. Run the Docker Container
\\\ash
docker run -p 5000:5000 devops-project-8
\\\

### 4. Access the Application
Open your browser and navigate to:
?? **http://localhost:5000**

---

## ?? API Endpoints
- **\GET /\** - Loads the interactive Web Dashboard.
- **\POST /alert\** - Ingests external webhook alerts.
- **\GET /api/incidents\** - Returns all logged incidents in JSON format.
- **\POST /trigger-demo\** - Simulates and adds a test incident via UI.
