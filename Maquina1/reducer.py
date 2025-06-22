#!/usr/bin/env python3
import sys
import json

total_likes = 0
total_downloads = 0
total_historic = 0

for line in sys.stdin:
    try:
        _, likes, downloads, historic = line.strip().split("\t")
        total_likes += int(likes)
        total_downloads += int(downloads)
        total_historic += int(historic)
    except:
        continue

resultado = {
    "totalLikes": total_likes,
    "totalDownloads": total_downloads,
    "totalHistoricDownloads": total_historic
}

# Escribe como JSON una sola línea
print(json.dumps(resultado))

