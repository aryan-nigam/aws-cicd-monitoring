
#!/bin/bash
set -e

if [ -f /opt/aws-cicd-monitoring/app.pid ]; then
    PID=$(cat /opt/aws-cicd-monitoring/app.pid)

    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"

        for i in {1..10}; do
            if ! kill -0 "$PID" 2>/dev/null; then
                break
            fi
            sleep 1
        done

        if kill -0 "$PID" 2>/dev/null; then
            kill -9 "$PID"
        fi
    fi

    rm -f /opt/aws-cicd-monitoring/app.pid
fi

exit 0
