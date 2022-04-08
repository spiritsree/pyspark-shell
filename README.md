# Pyspark Shell

[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/spiritsree/pyspark-shell)](https://hub.docker.com/r/spiritsree/pyspark-shell)
[![Docker Pulls](https://img.shields.io/docker/pulls/spiritsree/pyspark-shell)](https://hub.docker.com/r/spiritsree/pyspark-shell/tags)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/spiritsree/pyspark-shell?sort=semver)](https://hub.docker.com/r/spiritsree/pyspark-shell)

An interactive pyspark-shell in docker

## Quick Start

You can run this by just running the following

```
$ docker run --rm -ti --name pyspark-shell \
             spiritsree/pyspark-shell:latest
```

This will give a spark shell to work on.

```
###########################################################
#                     Spark 3.2.1                         #
#                                                         #
#      Spark session can be accessed using "SPARK"        #
#                                                         #
###########################################################


>>>
```

## Load CSV

For loading csv to work on mount the directory containing CSV files as `/data`

```
$ docker run --rm -ti --name pyspark-shell \
             -v /locat/dir:/data \
             spiritsree/pyspark-shell:latest
```

For changing log level pass the env variable as follows

## Custom log levels

```
$ docker run --rm -ti --name pyspark-shell \
             -v /locat/dir:/data \
             -e LOG_LEVEL=debug \
             spiritsree/pyspark-shell:latest
```

Supported log levels are `all`, `debug`, `error`, `fatal`, `trace`, `warn`, `info`, `off`.

## ORC/Parquet file type

```
$ docker run --rm -ti --name pyspark-shell \
             -v /locat/dir:/data \
             -e FILE_TYPE=orc \
             spiritsree/pyspark-shell:latest

$ docker run --rm -ti --name pyspark-shell \
             -v /locat/dir:/data \
             -e FILE_TYPE=parquet \
             spiritsree/pyspark-shell:latest
```

## Common Spark Dataframe Functions

**Count**

Count the number of rows

```
>>> DF.count()
30
```

**Show**

Displays data (will show only first 10 or 20 rows) if not specified.

```
>>> DF.show(5)
+---+---+---+---+
|_c1|_c2|_c3|_c4|
+---+---+---+---+
|  1| d1|  1|  d|
|  2| d2|  2|  d|
|  3| d3|  3|  d|
|  4| d4|  4|  d|
|  5| d5|  5|  d|
+---+---+---+---+
only showing top 5 rows
```

**Columns**

Show the header list.

```
>>> DF.columns
['_c1', '_c2', '_c3', '_c4']
```

**PrintSchema**

Shows the schema of data.

```
>>> DF.printSchema()
root
 |-- _c1: string (nullable = true)
 |-- _c2: string (nullable = true)
 |-- _c3: string (nullable = true)
 |-- _c4: string (nullable = true)
 ```

**Select**

Select based on expression.

```
>>> DF.select(DF._c1).show(2)
+---+
|_c1|
+---+
|  1|
|  2|
+---+
only showing top 2 rows
```

## Reference

* [Apache Spark](https://github.com/apache/spark)
* [Pyspark API reference](https://spark.apache.org/docs/latest/api/python/reference/index.html)
