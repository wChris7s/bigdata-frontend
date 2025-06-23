from confluent_kafka import Consumer
import json
import os
import subprocess

# Configuración
TOPIC = ''
CARPETA_HDFS = '/user/jav1/TrabajoFinalhdfsJSON'
ARCHIVO_NDJSON_LOCAL = '/tmp/kafka_json_azure/acumulador.json'

AZURE_BOOTSTRAP_SERVER = ''
AZURE_USERNAME = ''
AZURE_PASSWORD = ''

os.makedirs('/tmp/kafka_json_azure', exist_ok=True)

# Configurar consumidor Kafka
consumer = Consumer({
    'bootstrap.servers': AZURE_BOOTSTRAP_SERVER,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': AZURE_USERNAME,
    'sasl.password': AZURE_PASSWORD,
    'group.id': 'azure-consumer-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])
print(f"[✓] Conectado a Azure Event Hub (Kafka) escuchando el topic '{TOPIC}'...\n")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"[✗] Error: {msg.error()}")
            continue

        try:
            data = json.loads(msg.value().decode('utf-8'))

            # Agregar el JSON como línea a acumulador.json (NDJSON)
            with open(ARCHIVO_NDJSON_LOCAL, 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

            # Nombre único por timestamp para evitar sobrescritura en HDFS
            nombre_archivo_hdfs = f"ndjson_{os.getpid()}_{int(os.path.getmtime(ARCHIVO_NDJSON_LOCAL))}.json"

            resultado = subprocess.run(
                ['hdfs', 'dfs', '-put', '-f', ARCHIVO_NDJSON_LOCAL, f"{CARPETA_HDFS}/{nombre_archivo_hdfs}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if resultado.returncode == 0:
                print(f"[↑] Subido NDJSON a HDFS: {CARPETA_HDFS}/{nombre_archivo_hdfs}")
                os.remove(ARCHIVO_NDJSON_LOCAL)  # Limpiar archivo local tras subida
            else:
                print(f"[✗] Error al subir archivo:\n{resultado.stderr}")

        except Exception as e:
            print(f"[✗] Error procesando mensaje:\n{e}")

except KeyboardInterrupt:
    print("\n[!] Interrumpido por el usuario")

finally:
    consumer.close()

