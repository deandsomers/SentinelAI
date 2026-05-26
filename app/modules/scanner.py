from app.modules.parser import normalize_log
from app.modules.analyzer import analyze_log

def scan_log(log):
    normalized_log = normalize_log(log)
    analysis_result = analyze_log(normalized_log)
    return analysis_result