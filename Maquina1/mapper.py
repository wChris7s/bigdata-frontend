#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        likes = 1 if data.get("like") else 0
        downloads = data.get("downloads", 0)
        historic = data.get("historicDownloads", 0)

        print(f"likes\t{likes}")
        print(f"downloads\t{downloads}")
        print(f"historicDownloads\t{historic}")
    except Exception as e:
        pass  # Silenciar errores por si no es una línea JSON válida

