
#!/bin/bash
set -e

APP_DIR="/opt/aws-cicd-monitoring"
cd "$APP_DIR"

mkdir -p logs

nohup "$APP_DIR/venv/bin/python" -u -c \
'from app import app; app.run(host="0.0.0.0", port=5000)' \
>> "$APP_DIR/logs/application.log" 2>&1 &

echo $! > "$APP_DIR/app.pid"

sleep 2

if ! kill -0 "$(cat "$APP_DIR/app.pid")" 2>/dev/null; then
    cat "$APP_DIR/logs/application.log"
    exit 1
fi
