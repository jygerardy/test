# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs as SparkSQL dataframes Compute a SparkSQL dataframe to write into test

# Write recipe outputs
test = dataiku.Dataset("test")

