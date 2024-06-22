





### curl request

```bash
curl -X POST "http://localhost:8000/analyze_log" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "/path/to/your/logfile.log"}'

```

save the output to a file:
```bash

curl -X POST "http://localhost:8000/analyze_log" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "/path/to/your/logfile.log"}' \
     > analysis_results.json

```