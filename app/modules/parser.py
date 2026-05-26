def normalize_log(log):
    return log.strip().lower()

def retrieveIPAddress(log):
    return log.split(' ')[-1]