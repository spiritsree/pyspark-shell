import sys
import os
import re
import json
import hashlib
from datetime import datetime, timedelta
from collections import OrderedDict
from py4j.protocol import Py4JJavaError
from pyspark.context import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

class ConfigContext:
    '''
    Global configs
    '''
    def __init__(self):
        '''
        Initialize global configs.
        '''
        self.log_level = self.environ_or_default('LOG_LEVEL', 'info')

    @classmethod
    def environ_or_default(cls, env, default):
        '''
        Get the variable from environment or none
        '''
        try:
            return os.environ[env]
        except:
            return default

CONFIG = ConfigContext()
spark_context = SparkContext('local')
spark_context.setLogLevel(CONFIG.log_level.upper())
SPARK = SparkSession(spark_context)

data_dir = '/data'
files_to_load = []

for path, subdirs, files in os.walk(data_dir):
    for f_name in files:
        if re.match(r'.*?\.csv$', f_name):
            files_to_load.append(os.path.join(path, f_name))

if not files_to_load:
    print('')
    print('')
    print('###########################################################')
    print('#                     Spark {ver}                         #'.format(ver=SPARK.version))
    print('#                                                         #')
    print('#      Spark session can be accessed using "SPARK"        #')
    print('#                                                         #')
    print('###########################################################')
    print('')
    print('')
else:
    DF = SPARK.read.csv(files_to_load,
                                header=True,
                                quote='"',
                                escape='"',
                                mode="FAILFAST",
                                multiLine=True)

    print('')
    print('')
    print('###########################################################')
    print('#                     Spark {ver}                         #'.format(ver=SPARK.version))
    print('#                                                         #')
    print('#       csv files are loaded in to dataframe "DF"         #')
    print('#                                                         #')
    print('###########################################################')
    print('')
    print('')
