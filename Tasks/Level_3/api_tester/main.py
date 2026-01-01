from tester.runner import run_test
from tester.report import save_report
import json

try:
    with open("config/test.json", "r") as f:
        tests = json.load(f)["tests"]

    results = []

    for test in tests:
        result = run_test(test)
        results.append(result)

    save_report(results)

except Exception as e:
    print(e)
 