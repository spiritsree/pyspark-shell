#!/bin/bash

python_bin=$(command -v python)
python3_bin=$(command -v python3)
if [[ -z "${python_bin}" ]]; then
    ln -s "${python3_bin}" /usr/bin/python
fi

if [[ ! -d "/data" ]]; then
    mkdir /data
fi

export JAVA_HOME=$(dirname "$(dirname "$(readlink -f "$(which javac || which java)")")")
export PATH=${PATH}:${JAVA_HOME}/bin

# curl http://apache.mirror.anlx.net/spark/spark-2.4.5/spark-2.4.5-bin-without-hadoop.tgz -o spark.tgz

pyspark --version
