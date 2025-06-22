#!/bin/bash

while true; do
    echo "=== Ejecutando MapReduce $(date) ==="

    hdfs dfs -rm -r -skipTrash /user/jav1/resultadosFinal > /dev/null 2>&1

    hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
        -files mapper.py,reducer.py \
        -mapper "python3 mapper.py" \
        -reducer "python3 reducer.py" \
        -input /user/jav1/TrabajoFinalhdfsJSON \
        -output /user/jav1/resultadosFinal 2>&1 | grep --line-buffered -E "Running job|map [0-9]+% reduce [0-9]+%|completed successfully"

    echo "=== Análisis finalizado $(date) ==="
    echo "=== Esperando 70 segundos... ==="
    sleep 70
done

