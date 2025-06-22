#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        likes = data.get("likes", 0)
        downloads = data.get("downloads", 0)
        historic = data.get("historicLikes", 0)
        print(f"total\t{likes}\t{downloads}\t{historic}")
    except Exception:
        continue

