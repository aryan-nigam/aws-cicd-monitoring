**\# AWS CI/CD and Application Monitoring Pipeline**



**\## Overview**



A hands-on DevOps/SRE portfolio project that demonstrates automated Python testing, CI build automation, application health checks, and log-based troubleshooting.



**\## Architecture**



GitHub → AWS CodeBuild → Amazon S3



The Flask application and health-monitoring script can also run locally for availability checks and failure simulation.



**\## Technologies Used**



\- \*\*Python and Flask\*\* — application development

\- \*\*pytest\*\* — automated testing

\- \*\*Git and GitHub\*\* — source control

\- \*\*AWS CodeBuild\*\* — automated build and test execution

\- \*\*Amazon S3\*\* — build artifact storage

\- \*\*Linux Bash\*\* — deployment scripts prepared for EC2

\- \*\*Application monitoring and logging\*\* — health checks and incident simulation



**\## Features**



\- Flask home page and `/health` endpoint

\- Automated tests for application responses

\- CodeBuild pipeline configured through `buildspec.yml`

\- Build artifacts stored in Amazon S3

\- Periodic application health checks using `monitor.py`

\- Timestamped monitoring logs written to `monitor.log`

\- Failure simulation by stopping the Flask application

\- Deployment configuration prepared using `appspec.yml` and Bash scripts



**\## Application Endpoints**



| Endpoint | Purpose |

|---|---|

| `/` | Returns the application status message |

| `/health` | Returns JSON health status |



**Example health response:**



```json

{"status": "UP"}

```



**\## Run Locally**



**\### 1. Clone the repository**



```bash

git clone <YOUR\_GITHUB\_REPOSITORY\_URL>

cd aws-cicd-monitoring

```



Replace the placeholder with your actual GitHub repository URL.



**\### 2. Create and activate a virtual environment**



On Windows:



```bat

python -m venv venv

venv\\Scripts\\activate

```


**
\### 3. Install dependencies and run tests**



```bash

pip install -r requirements.txt

python -m pytest -v

```



**\### 4. Start the application**



```bash

python app.py

```



Open `http://127.0.0.1:5000/health` in your browser.



**\### 5. Run the monitoring script**



In a second terminal, activate the virtual environment and run:



```bash

python monitor.py

```



The monitor checks the health endpoint every 10 seconds and writes timestamped results to `monitor.log`.



**\## CI/CD Workflow**



1\. Source code is maintained in GitHub.

2\. AWS CodeBuild retrieves the repository and executes the commands in `buildspec.yml`.

3\. pytest validates the application.

4\. Build artifacts are uploaded to the configured Amazon S3 bucket.



**\## Deployment Status**



The CodeDeploy configuration files and deployment scripts have been prepared. Automated deployment to EC2 has not yet been completed because CodeDeploy access is restricted by the current AWS account plan.



**\## Future Improvements**



\- Complete automated deployment when an appropriate deployment target is available

\- Add metrics dashboards and alerting

\- Introduce structured application logs

\- Add monitoring for response time and availability

\- Integrate infrastructure provisioning with Terraform



**\## Learning Outcomes**



This project demonstrates practical experience with CI automation, automated testing, health endpoints, application monitoring, log analysis, and basic incident troubleshooting.

