# 📊 Proyecto Final Big Data - Sistema de Reacciones en Tiempo Real

Este proyecto implementa un sistema distribuido que permite a los usuarios dar **like o dislike** a imágenes. Las reacciones se procesan en tiempo real mediante Kafka y Flink, y también se almacenan en HDFS usando Flume para análisis batch.

---

##  Requisitos para el Frontend

Para que el frontend funcione correctamente en Angular, debes tener instalado lo siguiente:

- Node.js **v20.19.0**
- npm **10.x.x**
- Angular CLI

###  Instalación

```bash
# Instala curl si no lo tienes
sudo apt install curl

# Añade Node.js v20.x
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Instala Angular CLI globalmente
sudo npm install -g @angular/cli
pip3 install confluent-kafka==1.5.0

# para las paginas
pip install fastapi uvicorn

```
Una vez instalado, ejecuta el frontend con:

```bash
jps  # Debe mostrar: NameNode
cd bigdata-frontend
npm install
ng serve
```

Iniciar el Clúster

1.-Hadoop
```bash
# maquina1
start-all.sh
stop-all.sh
ng serve
```
2.-Flink
```bash
# maquina1
/usr/local/flink/bin/start-cluster.sh
/usr/local/flink/bin/stop-cluster.sh

```
3.-kafka
```bash
# maquina1
cd /usr/local/kafka
# Iniciar Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
# Iniciar el broker
bin/kafka-server-start.sh config/server.properties
# maquina2 y 3
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties

cd /usr/local/kafka
bin/zookeeper-shell.sh localhost:2181
ls /brokers/ids

```

4.-Activar microservicios

antes de activar los microservicios:
Desactivar savemode del cluster:
```bash
hdfs dfsadmin -safemode leave
```
Crear esta carpeta (solo una ves si no lo isieron)
```bash
hdfs dfs -mkdir -p /user/jav1/resultadosFinal
```

en maquina 3
```bash
# maquina3
python3 generador_json.py
python3 microservicio2_producer.py
```
en maquina 1
```bash
# maquina1
python3 consumer.py
python3 microservicioJSON.py
```
para verifivar si se estan creando en la carpeta los archivos json colocar:
```bash
hdfs dfs -ls /user/jav1/TrabajoFinalhdfsJSON
```
para verifivar si se estan creando los resultados generales usar:

```bash
hdfs dfs -ls /user/jav1/resultadosFinal
```
para dar permisos de hadoop:
```bash
chmod +x mapper.py reducer.py
chmod +x ejecutar_periodicamente.sh

```
