

import time
import urllib.request
import urllib.error
from datetime import datetime
import csv
HEALTH_URL = "http://127.0.0.1:5000/health"
CHECK_INTERVAL = 10
LOG_FILE = "monitor.log"
CSV_FILE = "monitor_history.csv"

total_checks = 0
successful_checks = 0
failed_checks = 0

consecutive_failures = 0
alert_triggered = False
FAILURE_THRESHOLD = 3
RESPONSE_TIME_THRESHOLD_MS = 1000


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    print(log_message)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_message + "\n")


def save_history(status, http_status, response_time):
    file_exists = __import__("os").path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "status",
                "http_status",
                "response_time_ms",
                "total_checks",
                "successful_checks",
                "failed_checks",
                "consecutive_failures"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status,
            http_status,
            f"{response_time:.2f}",
            total_checks,
            successful_checks,
            failed_checks,
            consecutive_failures
        ])



def check_health():
    global total_checks, successful_checks, failed_checks
    global consecutive_failures, alert_triggered

    total_checks += 1
    start_time = time.perf_counter()

    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=5) as response:
            response_time = (time.perf_counter() - start_time) * 1000

            if response.status == 200:
                successful_checks += 1

                if consecutive_failures > 0:
                    write_log("RECOVERY - Application is responding again")

                consecutive_failures = 0
                alert_triggered = False

                write_log(
                    f"HEALTHY | status={response.status} | "
                    f"response_time_ms={response_time:.2f} | "
                    f"successes={successful_checks} | failures={failed_checks}"
                )

                if response_time > RESPONSE_TIME_THRESHOLD_MS:
                    write_log(
                        f"WARNING - Slow response detected | "
                        f"response_time_ms={response_time:.2f} | "
                        f"threshold_ms={RESPONSE_TIME_THRESHOLD_MS}"
                )
                save_history("HEALTHY", response.status, response_time)

            else:
                failed_checks += 1
                consecutive_failures += 1

                write_log(
                    f"UNHEALTHY | status={response.status} | "
                    f"response_time_ms={response_time:.2f}"
                )
                save_history("UNHEALTHY", response.status, response_time)

    except (urllib.error.URLError, TimeoutError) as error:
        response_time = (time.perf_counter() - start_time) * 1000
        failed_checks += 1
        consecutive_failures += 1

        write_log(
            f"UNHEALTHY | error={error} | "
            f"response_time_ms={response_time:.2f} | "
            f"consecutive_failures={consecutive_failures}"
        )
        save_history("UNHEALTHY", "N/A", response_time)

    if consecutive_failures >= FAILURE_THRESHOLD and not alert_triggered:
        write_log(
            f"ALERT - Application failed {consecutive_failures} "
            "consecutive health checks"
        )
        alert_triggered = True



def main():
    write_log("Starting application health monitor")
    write_log(f"Health URL: {HEALTH_URL}")
    write_log(f"Check interval: {CHECK_INTERVAL} seconds")

    try:
        while True:
            check_health()

            if total_checks > 0:
                availability = (successful_checks / total_checks) * 100
                write_log(
                    f"SUMMARY | checks={total_checks} | "
                    f"availability={availability:.2f}%"
                )

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        write_log("Health monitor stopped")
        write_log(
            f"FINAL SUMMARY | checks={total_checks} | "
            f"successes={successful_checks} | failures={failed_checks}"
        )


if __name__ == "__main__":
    main()
