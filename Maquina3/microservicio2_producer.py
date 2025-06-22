  import os
import json
import random
import uuid

# Carpeta donde se guardarán los archivos
carpeta = "data"
os.makedirs(carpeta, exist_ok=True)

# Datos base
descripciones = [
    "A lush greenhouse filled with greenery.",
    "Sunset over a peaceful mountain lake.",
    "Abstract painting with vibrant colors.",
    "City skyline on a foggy morning.",
    "Close-up of dew on a spider web."
]

tags_base = [
    "land", "plant", "garden", "leaf", "spain", "gardening", "path", "rainforest",
    "outdoors", "pottery", "herbs", "greenhouse", "vase", "backyard", "vegetation",
    "potted plant", "jar", "valencia", "yard", "herbal"
]

# Generador principal
while True:
    nombre = input("Ingrese un nombre para el archivo (o 0 para salir): ")

    if nombre == "0":
        print("Programa finalizado.")
        break

    # Crear datos aleatorios
    data = {
        "username": f"{random.choice(['bright', 'dark', 'swift', 'mighty', 'lazy'])}-"
                    f"{random.choice(['tiger', 'eagle', 'lion', 'fox'])}-"
                    f"{random.randint(100, 999)}",
        "like": random.choice([True, False]),
        "imageDescription": random.choice(descripciones),
        "historicLikes": random.randint(0, 500),
        "historicDownloads": random.randint(100, 10000),
        "tags": random.sample(tags_base, k=random.randint(5, len(tags_base)))
    }

    # Guardar en archivo JSON
    ruta = os.path.join(carpeta, f"{nombre}.json")
    with open(ruta, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Archivo '{ruta}' generado con éxito.\n")

