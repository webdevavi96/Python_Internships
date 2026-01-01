from datetime import datetime


def save_report(result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    cunstruct_filename = f"reports/{timestamp}_report.txt"
    with open(cunstruct_filename, "w") as f:
        for res in result:
            line = f"{res["name"]} | Status: {res["status"]} | Success: {res["success"]} | Response Time: {res["response_time"]}\n"
            f.write(line)
 