# Data Generator and API Server

This project consists of two main components:
1. A Flask server that exposes an API for `app1`.
2. A telemetry data generator for `app2`.

## Directory Structure
```
Data-Generator
├── docker-compose.yml
├── Dockerfile.app1
├── Dockerfile.app2
├── pyproject.toml
├── README.md
├── requirements.txt
└── src
    ├── app1
    │   ├── api_server.py
    │   ├── static
    │   │   └── swagger.yaml
    │   └── templates
    │       └── index.html
    └── app2
        └── telemetry_generator.py
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/miroslawsteblik/data-generator
    cd data-generator
    ```

2. Build and start the Docker containers:
    ```sh
    docker compose up --build -d
    ```

### Usage

- The Flask server for `app1` will be available at `http://localhost:5000`.
- The telemetry data generator for `app2` will be available at `http://localhost:5001`.

### Configuration

Logging is configured to use the DEBUG level:
```python
logging.basicConfig(level=logging.DEBUG)
```

### API Endpoints

> app1 API Server
 - GET /api/telemetry
 - POST /api/telemetry 

> app2 Telemetry Data Generator
 - Generates telemetry data and sends it to the app1 API server.

### Troubleshooting
If you encounter any issues, try the following steps:

1. Ensure Docker and Docker Compose are installed and running.
2. Rebuild the Docker container
```
docker-compose down
docker-compose up --build
```

 #### Getting Data from the API

 ```
import requests

url = "http://localhost:5000/api/telemetry"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Received data:", data)
else:
    print("Failed to get data:", response.status_code)
```