log = input("Enter log message: ")

if "failed" in log:
    print("Possible brute-force attempt")

elif "virus" in log:
    print("Possible malware detected")

elif "unauthorized" in log:
    print("Unauthorized access attempt")

else:
    print("No known threats detected")
