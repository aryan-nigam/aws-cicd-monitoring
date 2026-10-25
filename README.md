# SRE Monitoring and AWS CI/CD Pipeline

A hands-on project demonstrating application health monitoring, failure detection, response-time tracking, containerization, automated testing, and a CI pipeline using AWS CodeBuild.

## Project Overview

This project runs a Python Flask application with a health-check endpoint and a custom monitoring script. Monitoring results are recorded in a CSV file, analyzed through a reporting script, and visualized in a Streamlit dashboard.

The application is packaged using Docker, while GitHub and AWS CodeBuild are used for source control and automated testing.

## Architecture

Developer → GitHub Repository → AWS CodeBuild → Automated Tests

Local Application → Docker Container → Health Monitor → CSV History → Monitoring Report and Dashboard

## Features

- **Application health checks:** Checks the Flask application's `/health` endpoint.
- **Failure detection:** Identifies consecutive failed health checks and generates an alert after a configurable threshold.
- **Recovery detection:** Logs when the application starts responding again.
- **Response-time monitoring:** Measures HTTP response time and warns when it exceeds a configured threshold.
- **CSV monitoring history:** Records health-check status, response time, and check counters.
- **Monitoring report:** Calculates availability, successful and failed checks, and average response time.
- **Interactive dashboard:** Uses Streamlit and Pandas to display metrics, charts, and recent health-check records.
- **Docker containerization:** Packages the Flask application and its Python dependencies into a container image.
- **Automated testing:** Uses pytest to test the application endpoints.
- **CI pipeline:** Uses AWS CodeBuild to install dependencies and run automated tests.

## Technology Stack

- Python
- Flask
- pytest
- Streamlit
- Pandas
- Docker
- Git and GitHub
- AWS CodeBuild
- Amazon S3 for build artifacts

## Project Structure

```text
aws-cicd-monitoring/
├── app.py
├── monitor.py
├── report.py
├── dashboard.py
├── tests/
│   └── test_app.py
├── scripts/
│   ├── install_app.sh
│   ├── start_app.sh
│   └── stop_app.sh
├── appspec.yml
├── buildspec.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Start the Flask application

```bash
python app.py
```

The application runs at `http://localhost:5000`.

Health endpoint: `http://localhost:5000/health`

Expected response:

```json
{"status": "UP"}
```

### 3. Start the monitoring script

Open a second terminal and run:

```bash
python monitor.py
```

The script periodically checks application health, records monitoring events, and detects failures and recovery.

### 4. Generate a monitoring report

```bash
python report.py
```

### 5. Start the dashboard

```bash
python -m streamlit run dashboard.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Run with Docker

Build the Docker image:

```bash
docker build -t aws-cicd-monitoring:1.0 .
```

Start the container:

```bash
docker run --rm -d --name sre-monitor -p 5000:5000 aws-cicd-monitoring:1.0
```

Verify application health:

```bash
curl http://localhost:5000/health
```

View container logs:

```bash
docker logs sre-monitor
```

Stop the container:

```bash
docker stop sre-monitor
```

## Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

The tests verify the home endpoint and health endpoint responses.

## AWS CI Pipeline

The GitHub repository is connected to AWS CodeBuild. The build process installs the Python dependencies and runs the pytest test suite using `buildspec.yml`.

A successful CodeBuild execution has been verified.

Amazon S3 is used to store build artifacts.

**Deployment status:** The CodeDeploy deployment workflow has not been completed. The project currently demonstrates automated testing through CodeBuild and local Docker execution, rather than a completed production deployment on AWS.

## Future Improvements

- Integrate centralized monitoring and alerting.
- Add infrastructure provisioning with Terraform.
- Deploy the application to a cloud environment.
- Add container orchestration and service health checks.
- Improve test coverage and pipeline automation.

## Learning Outcomes

This project provided hands-on practice with Python application monitoring, incident detection, response-time metrics, availability calculations, Docker, automated testing, GitHub workflows, and AWS CodeBuild.

## Author

Aryan Nigam

GitHub: https://github.com/aryan-nigam


