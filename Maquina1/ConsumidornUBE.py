from confluent_kafka import Consumer
import json
import os
import uuid
import subprocess

# Configuración de Azure Kafka
TOPIC = ''
CARPETA_HDFS = '/user/jav1/TrabajoFinalhdfsJSON'
CARPETA_TEMP = '/tmp/kafka_json_azure'

# Connection string
AZURE_BOOTSTRAP_SERVER = ''
AZURE_USERNAME = ''
AZURE_PASSWORD = ''

os.makedirs(CARPETA_TEMP, exist_ok=True)

# Configuración del consumidor
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
            nombre_archivo = f"{uuid.uuid4()}.json"
            ruta_local = os.path.join(CARPETA_TEMP, nombre_archivo)

            with open(ruta_local, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            resultado = subprocess.run(
                ['hdfs', 'dfs', '-put', ruta_local, f"{CARPETA_HDFS}/{nombre_archivo}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if resultado.returncode == 0:
                print(f"[↑] Subido a HDFS: TrabajoFinalhdfsJSON/{nombre_archivo}")
            else:
                print(f"[✗] Error al subir {nombre_archivo}:\n{resultado.stderr}")

            os.remove(ruta_local)

        except Exception as e:
            print(f"[✗] Error procesando mensaje:\n{e}")

except KeyboardInterrupt:
    print("\n[!] Interrumpido por el usuario")

finally:
    consumer.close()

