from datetime import datetime
import json

def generate_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def save_scan_results(log):
    with open('logs/scan_results.log','w') as scan_file:
        scan_file.writelines(json.dumps(log,indent=4))