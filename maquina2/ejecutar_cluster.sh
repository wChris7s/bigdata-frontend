#!/bin/bash

# Ejecutar scripts en maquina3
ssh jav3@192.168.1.103 'bash -c "
  cd /home/jav3/Escritorio &&
  nohup python3 microservicio2_producer.py > producer.log 2>&1 &
  sleep 2
  nohup python3 generador_json.py > generador.log 2>&1 &
"'

# Ejecutar scripts en maquina1
ssh jav1@192.168.1.101 'bash -c "
  cd /home/jav1/Escritorio &&
  nohup python3 consumer.py > consumer.log 2>&1 &
  sleep 2
  nohup python3 microservicio1.py > micro1.log 2>&1 &
"'

echo "✅ Todos los servicios fueron lanzados."

