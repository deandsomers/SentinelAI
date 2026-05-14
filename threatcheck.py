log_message = input("Enter log message: ")

if "failed" in log_message:
    print("Possible brute-force attempt")

elif "virus" in log_message:
    print("Possible malware detected")

elif "unauthorized" in log_message:
    print("Unauthorized access attempt")

else:
    print("No known threats detected")