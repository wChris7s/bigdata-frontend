from kafka import KafkaConsumer
import json
import os
import subprocess
import uuid

# Configuración
KAFKA_BROKER = '192.168.1.101:9092'
TOPIC = 'interacciones-imagenes'
CARPETA_HDFS = '/user/jav1/TrabajoFinalhdfsJSON'
CARPETA_TEMP = '/tmp/kafka_json_temp'

os.makedirs(CARPETA_TEMP, exist_ok=True)

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo-consumidor-1',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print(f"[✓] Escuchando el topic '{TOPIC}' en {KAFKA_BROKER} y subiendo a HDFS...\n")

for mensaje in consumer:
    try:
        contenido = mensaje.value
        nombre_archivo = f"{uuid.uuid4()}.json"
        ruta_local = os.path.join(CARPETA_TEMP, nombre_archivo)

        # Guardar temporalmente
        with open(ruta_local, 'w', encoding='utf-8') as f:
            json.dump(contenido, f, ensure_ascii=False, indent=4)

        # Subir a HDFS con resultado visible
        resultado = subprocess.run(
            ['hdfs', 'dfs', '-put', ruta_local, f"{CARPETA_HDFS}/{nombre_archivo}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if resultado.returncode == 0:
            print(f"[↑] Archivo subido a HDFS: {CARPETA_HDFS}/{nombre_archivo}")
        else:
            print(f"[✗] Error al subir archivo a HDFS:")
            print(resultado.stderr)

        os.remove(ruta_local)

    except Exception as e:
        print(f"[✗] Error general procesando mensaje: {e}")

