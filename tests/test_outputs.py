import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

def test_criterion_1_file_exists_and_valid_json():
    """Verifies Success Criterion 1: The output file report.json must be saved 
    at the absolute path `/app/report.json` and must be structurally valid JSON.
    """
    assert REPORT_PATH.exists(), "The summary output file /app/report.json was not generated."
    
    try:
        with open(REPORT_PATH, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        assert False, "The generated report.json file does not contain clean, valid JSON data."
        
    required_keys = ["total_requests", "unique_ips", "top_path"]
    for key in required_keys:
        assert key in data, f"Required summary schema metric key '{key}' is missing from the output json."


def test_criterion_2_metric_values_match_log():
    """Verifies Success Criterion 2: The report must correctly calculate the log file metrics 
    where total_requests is 6, unique_ips is 3, and top_path is '/index.html'.
    """
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
        
    assert data["total_requests"] == 6, f"Expected 6 total requests, but log analysis reported {data['total_requests']}."
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, but log analysis reported {data['unique_ips']}."
    assert data["top_path"] == "/index.html", f"Expected top path to be '/index.html', but found '{data['top_path']}'."
