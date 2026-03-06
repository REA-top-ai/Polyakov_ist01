import json


def key_value(log):
    key =["date", "level"]
    value = log.split("|")
    part_1 = {key : value for key , value in zip(key, value[:2])}
    part_2 = dict((elements.split("=") for elements in value[2].split()))

    for key , value in part_2.items():
        if value.isdigit():
            part_2[key] = int(value)

    return part_1 | part_2

def write_json(logs, save_file = None):
    glossary = [key_value(log) for log in logs]
    if save_file:
        with open(save_file, "w", encoding="utf-8") as f:
            json.dump(glossary, f, indent=4, ensure_ascii=False)
    return glossary

def level_chek(logs,level):

    return [log for log in logs if log.get("level") == level]

def count_by_level(logs):
    result = {}

    for log in logs:
        level = log["level"]
        result[level] = result.get(level, 0) + 1

    return result

def count_by_user(logs):
    result = {}

    for log in logs:
        user = log.get("user")
        result[user] = result.get(user, 0) + 1

    return result

def failed_payment_sum(logs):
    total = 0

    for log in logs:
        if log.get("action") == "payment" and log.get("status") == "fail":
            total += log.get("amount", 0)

    return total

logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

parsed_logs = write_json(logs)

print("---- COUNT BY LEVEL ----")
print(count_by_level(parsed_logs))

print("---- COUNT BY USER ----")
print(count_by_user(parsed_logs))

print("---- FAILED PAYMENT SUM ----")
print(failed_payment_sum(parsed_logs))