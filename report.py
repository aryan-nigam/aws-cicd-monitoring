
import csv
import os

CSV_FILE = "monitor_history.csv"


def generate_report():
    if not os.path.exists(CSV_FILE):
        print("No monitoring history found. Run monitor.py first.")
        return

    total_checks = 0
    successful_checks = 0
    failed_checks = 0
    response_times = []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_checks += 1

            if row["status"] == "HEALTHY":
                successful_checks += 1
            else:
                failed_checks += 1

            try:
                response_times.append(
                    float(row["response_time_ms"])
                )
            except (ValueError, KeyError):
                pass

    if total_checks == 0:
        print("The monitoring history is empty.")
        return

    availability = (successful_checks / total_checks) * 100

    average_response_time = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )

    print("\n===== APPLICATION MONITORING REPORT =====")
    print(f"Total checks           : {total_checks}")
    print(f"Successful checks      : {successful_checks}")
    print(f"Failed checks          : {failed_checks}")
    print(f"Availability           : {availability:.2f}%")
    print(f"Average response time  : {average_response_time:.2f} ms")
    print("==========================================\n")


if __name__ == "__main__":
    generate_report()
