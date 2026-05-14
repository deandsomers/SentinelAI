def analyze_log(log_message):

    if "failed" in log_message:
        return "Possible brute-force attempt"

    elif "virus" in log_message:
        return "Possible malware detected"

    elif "unauthorized" in log_message:
        return "Unauthorized access attempt"

    else:
        return "No known threats detected"


user_log = input("Enter log message: ")

result = analyze_log(user_log)

print(result)