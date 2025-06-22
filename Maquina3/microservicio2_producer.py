import os
import json
import time
from kafka import KafkaProducer

# Configuración
KAFKA_BROKER = '192.168.1.101:9092'  # IP de tu broker Kafka
TOPIC = 'interacciones-imagenes'
CARPETA_DATA = 'data'  # Carpeta donde estarán los archivos .json

# Inicializar productor
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(f"[✓] Microservicio iniciado. Monitoreando la carpeta '{CARPETA_DATA}' cada 2 segundos...")

# Bucle de revisión continua
while True:
    try:
        archivos = [f for f in os.listdir(CARPETA_DATA) if f.endswith('.json')]

        for archivo in archivos:
            ruta_archivo = os.path.join(CARPETA_DATA, archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            # Enviar a Kafka
            producer.send(TOPIC, datos)
            print(f"[→] JSON enviado a Kafka: {archivo}")

            # Eliminar archivo después de enviarlo
            os.remove(ruta_archivo)
            print(f"[✓] Archivo eliminado: {archivo}")

    except Exception as e:
        print(f"[✗] Error procesando archivos: {e}")

    time.sleep(2)

