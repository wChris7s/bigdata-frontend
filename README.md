# Bigdata
## darle permisos hdfs y archivos
```bash

hdfs dfsadmin -safemode leave
chmod +x mapper.py reducer.py
chmod +x ejecutar_periodicamente.sh

```

## activar solo en maquina 1 

ejecutar_periodicamente.sh
ConsumidornUBE.py

```bash
./ejecutar_periodicamente.sh
python3 ConsumerNube.py
```

verificar en el front los json creados y los resultados usando estos comandos
```bash
hdfs dfs -ls /user/jav1/TrabajoFinalhdfsJSON

hdfs dfs -ls /user/jav1/resultadosFinal

hdfs dfs -cat /user/jav1/TrabajoFinalhdfsJSON/*.json | head -n 5

hdfs dfs -cat /user/jav1/resultadosFinal/part-00000

```

