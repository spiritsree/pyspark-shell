'''
Pyspark shell with loaded files based on the type
Default: csv
'''
# pylint: disable=unused-import,import-error,wildcard-import,unused-variable
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
        self.file_type = self.environ_or_default('FILE_TYPE', 'csv')
        self.data_dir = '/data'

    @classmethod
    def environ_or_default(cls, env, default):
        '''
        Get the variable from environment or none
        '''
        try:
            return os.environ[env]
        except KeyError:
            return default

    @classmethod
    def environ_or_die(cls, env):
        '''
        Get the variable from environment or die
        '''
        try:
            return os.environ[env]
        except KeyError:
            sys.exit(1)

def read_files(data_dir, file_type):
    '''
    Load files from the /data dir based on type
    '''
    files_to_load = []
    for path, subdirs, files in os.walk(data_dir):
        for f_name in files:
            if file_type == 'csv':
                if re.match(r'.*?\.csv$', f_name):
                    files_to_load.append(os.path.join(path, f_name))
            elif file_type in ('orc', 'parquet'):
                regex_string = rf'.*?\.{file_type}$'
                if re.match(regex_string, f_name):
                    files_to_load.append(os.path.join(path, f_name))
    return files_to_load

CONFIG = ConfigContext()
SPARK_CONTEXT = SparkContext('local')
SPARK_CONTEXT.setLogLevel(CONFIG.log_level.upper())
SPARK = SparkSession(SPARK_CONTEXT)

def main():
    '''
    Main function
    '''
    files_to_load = read_files(CONFIG.data_dir, CONFIG.file_type)
    desc_string = 'Spark session can be accessed using "SPARK"'
    data_frame = ''
    if files_to_load:
        try:
            if CONFIG.file_type == 'csv':
                data_frame = SPARK.read.csv(files_to_load,
                                header=True,
                                quote='"',
                                escape='"',
                                mode="FAILFAST",
                                multiLine=True)
            elif CONFIG.file_type == 'orc':
                data_frame = SPARK.read.orc(files_to_load)
            elif CONFIG.file_type == 'parquet':
                data_frame = SPARK.read.parquet(files_to_load)
            desc_string = f' Files of type {CONFIG.file_type} are loaded in to dataframe "DF" '
        except Py4JJavaError as load_err:
            print(f'{load_err}')
            print('Fix the error and re-run or you can use the default spark session')
    vers_string = f'Spark {SPARK.version}'
    hash_string = '#'
    null_string = ''
    print('')
    print('')
    print(f'{hash_string:#^70}')
    print('#' + vers_string.center(68) + '#')
    print('#' + null_string.center(68) + '#')
    print('#' + desc_string.center(68) + '#')
    print('#' + null_string.center(68) + '#')
    print(f'{hash_string:#^70}')
    print('')
    print('')
    return data_frame

DF = main()
