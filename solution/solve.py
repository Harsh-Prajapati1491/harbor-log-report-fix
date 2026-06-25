import json
import re
from pathlib import Path
from collections import Counter

def main():
    log_path = Path("/app/access.log")
    report_path = Path("/app/report.json")
    
    paths = Counter()
    ips = set()
    total_requests = 0
    
    if log_path.exists():
        with open(log_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                total_requests += 1
                parts = line.split()
                if parts:
                    ips.add(parts[0])
                
                match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
                if match:
                    paths[match.group(1)] += 1

    top_path = paths.most_common(1)[0][0] if paths else ""
    
    output_data = {
        "total_requests": total_requests,
        "unique_ips": len(ips),
        "top_path": top_path
    }
    
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as out_file:
        json.dump(output_data, out_file)
        
    print(f"Successfully compiled metrics and wrote summary report to {report_path}")

if __name__ == "__main__":
    main()
