import subprocess
import json
import os
import time
import uuid
import matplotlib.pyplot as plt
import pandas as pd

# Rutas relativas al script
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_HDFS = '/user/jav1/TrabajoFinalhdfsJSON'
CARPETA_LOCAL = os.path.join(RUTA_BASE, 'tmp_hdfs_json')
CARPETA_IMAGENES = os.path.join(RUTA_BASE, 'resultados')

# Crear carpetas si no existen
os.makedirs(CARPETA_LOCAL, exist_ok=True)
os.makedirs(CARPETA_IMAGENES, exist_ok=True)

def descargar_archivos_hdfs():
    subprocess.run(['hdfs', 'dfs', '-get', f'{CARPETA_HDFS}/*', CARPETA_LOCAL],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def eliminar_archivos_hdfs():
    subprocess.run(['hdfs', 'dfs', '-rm', f'{CARPETA_HDFS}/*'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def procesar_datos_y_generar_grafico():
    likes = []
    downloads = []

    for archivo in os.listdir(CARPETA_LOCAL):
        if archivo.endswith('.json'):
            with open(os.path.join(CARPETA_LOCAL, archivo), 'r', encoding='utf-8') as f:
                data = json.load(f)
                likes.append(data.get('historicLikes', 0))
                downloads.append(data.get('historicDownloads', 0))
            os.remove(os.path.join(CARPETA_LOCAL, archivo))  # borrar local

    if likes and downloads:
        df = pd.DataFrame({
            'Imagen': [f'img_{i+1}' for i in range(len(likes))],
            'Likes': likes,
            'Downloads': downloads
        })

        df.set_index('Imagen').plot(kind='bar', figsize=(10, 6))
        plt.title('Likes y Downloads por Imagen')
        plt.ylabel('Cantidad')
        plt.tight_layout()

        nombre_imagen = os.path.join(CARPETA_IMAGENES, f'grafico_{uuid.uuid4()}.png')
        plt.savefig(nombre_imagen)
        plt.close()
        print(f"[✓] Imagen guardada en: {nombre_imagen}")
    else:
        print("[ℹ] No hay archivos JSON nuevos para procesar.")

# Bucle que se repite cada 60 segundos
while True:
    print("[⏳] Iniciando ciclo de análisis...")
    descargar_archivos_hdfs()
    procesar_datos_y_generar_grafico()
    eliminar_archivos_hdfs()
    print("[✔] Ciclo finalizado. Esperando 60 segundos...\n")
    time.sleep(60)

