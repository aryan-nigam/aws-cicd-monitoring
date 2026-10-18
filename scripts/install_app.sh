
#!/bin/bash
set -e

APP_DIR="/opt/aws-cicd-monitoring"

mkdir -p "$APP_DIR"
cd "$APP_DIR"

python3 -m venv venv
"$APP_DIR/venv/bin/python" -m pip install --upgrade pip
"$APP_DIR/venv/bin/python" -m pip install -r requirements.txt
