
import time
import urllib.request
import urllib.error
from datetime import datetime

HEALTH_URL = "http://127.0.0.1:5000/health"
CHECK_INTERVAL = 10
LOG_FILE = "monitor.log"


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    print(log_message)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_message + "\n")


def check_health():
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=5) as response:
            if response.status == 200:
                write_log("HEALTHY - Application is UP")
            else:
                write_log(f"UNHEALTHY - HTTP {response.status}")

    except (urllib.error.URLError, TimeoutError) as error:
        write_log(f"UNHEALTHY - {error}")


if __name__ == "__main__":
    write_log("Starting application health monitor")
    write_log("Press Ctrl+C to stop")

    try:
        while True:
            check_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        write_log("Health monitor stopped")

