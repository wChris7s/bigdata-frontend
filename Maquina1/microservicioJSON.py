import subprocess
import json
import os
import time
import uuid

# Rutas
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_HDFS_ENTRADA = '/user/jav1/TrabajoFinalhdfsJSON'
CARPETA_HDFS_SALIDA = '/user/jav1/resultadosFinal'
CARPETA_LOCAL = os.path.join(RUTA_BASE, 'tmp_hdfs_json')
ARCHIVO_TOTAL_LOCAL = os.path.join(CARPETA_LOCAL, 'totales.json')

# Asegurarse de que existen carpetas locales
os.makedirs(CARPETA_LOCAL, exist_ok=True)

def descargar_archivos_hdfs():
    subprocess.run(['hdfs', 'dfs', '-get', f'{CARPETA_HDFS_ENTRADA}/*', CARPETA_LOCAL],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def eliminar_archivos_hdfs_entrada():
    subprocess.run(['hdfs', 'dfs', '-rm', f'{CARPETA_HDFS_ENTRADA}/*'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def subir_resultado_a_hdfs(archivo_local, nombre_destino):
    subprocess.run(['hdfs', 'dfs', '-mkdir', '-p', CARPETA_HDFS_SALIDA],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['hdfs', 'dfs', '-put', archivo_local, f'{CARPETA_HDFS_SALIDA}/{nombre_destino}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def procesar_totales_y_guardar_json():
    total_likes = 0
    total_downloads = 0
    total_historic = 0
    archivos = os.listdir(CARPETA_LOCAL)

    for archivo in archivos:
        if archivo.endswith('.json') and archivo != 'totales.json':
            with open(os.path.join(CARPETA_LOCAL, archivo), 'r', encoding='utf-8') as f:
                data = json.load(f)
                total_likes += 1 if data.get('like', False) else 0
                total_downloads += data.get('historicDownloads', 0)
                total_historic += data.get('historicLikes', 0)
            os.remove(os.path.join(CARPETA_LOCAL, archivo))  # Limpiar local

    if archivos:
        totales = {
            "totalLikes": total_likes,
            "totalDownloads": total_downloads,
            "totalHistoricDownloads": total_historic
        }

        with open(ARCHIVO_TOTAL_LOCAL, 'w', encoding='utf-8') as f:
            json.dump(totales, f, ensure_ascii=False, indent=4)

        nombre_hdfs = f'totales_{uuid.uuid4()}.json'
        subir_resultado_a_hdfs(ARCHIVO_TOTAL_LOCAL, nombre_hdfs)
        os.remove(ARCHIVO_TOTAL_LOCAL)
        print(f"[✓] Archivo de totales subido a HDFS: {CARPETA_HDFS_SALIDA}/{nombre_hdfs}")
    else:
        print("[ℹ] No se encontraron archivos JSON para procesar.")

# Bucle continuo
while True:
    print("[⏳] Iniciando ciclo de análisis de totales...")
    descargar_archivos_hdfs()
    procesar_totales_y_guardar_json()
    eliminar_archivos_hdfs_entrada()
    print("[✔] Ciclo finalizado. Esperando 60 segundos...\n")
    time.sleep(60)

