An Apache-style web access log file has been placed in your working environment at `/app/access.log`.

Your task is to analyze this log traffic data and generate an automated aggregate summary file. Parse the log file and compute metrics detailing the total traffic load, unique tracking nodes, and peak endpoint location.

Write your final summary directly to an absolute JSON output file at the following path:
`/app/report.json`

The JSON payload file must satisfy the following exact numbered success criteria:
1. The file must exist at the exact location `/app/report.json` and must be structurally valid JSON containing the metric keys "total_requests", "unique_ips", and "top_path".
2. The file must correctly calculate the log file metrics based on the provided data, where the value of "total_requests" is exactly 6, the value of "unique_ips" is exactly 3, and the value of "top_path" is exactly "/index.html".

Ensure that the resulting JSON file maps exactly to these parameters, matches the layout keys, and contains no trailing white space outside valid JSON text format.
