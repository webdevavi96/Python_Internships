import requests
import time


def run_test(test):
    start = time.time()

    res = requests.request(
        method=test["method"], url=test["url"], json=test.get("payload")
    )

    response_time = time.time() - start

    is_success = res.status_code == test["expected_status"]

    data = {
        "name": test["name"],
        "status": res.status_code,
        "success": is_success,
        "response_time": round(response_time, 2),
    }
    
    return data
