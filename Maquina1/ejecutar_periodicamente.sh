#!/bin/bash

while true
do
    echo "=== Ejecutando MapReduce $(date) ==="

    hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
      -input /user/jav1/TrabajoFinalhdfsJSON \
      -output /user/jav1/resultadosFinal \
      -mapper mapper.py \
      -reducer reducer.py \
      -file mapper.py \
      -file reducer.py

    echo "=== Esperando 70 segundos... ==="
    sleep 70
done

