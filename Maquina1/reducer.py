#!/usr/bin/env python3
import sys
import json

current_key = None
total = 0
results = {}

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        value = int(value)

        if key != current_key and current_key is not None:
            results[current_key] = total
            total = value
        else:
            total += value

        current_key = key
    except:
        continue

if current_key is not None:
    results[current_key] = total

print(json.dumps({
    "totalLikes": results.get("likes", 0),
    "totalDownloads": results.get("downloads", 0),
    "totalHistoricDownloads": results.get("historicDownloads", 0)
}))

