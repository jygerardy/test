# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
multilevel_index = dataiku.Dataset("multilevel_index")
#multilevel_index_df = multilevel_index.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

df = pd.read_csv('Users/jygerardy/Downloads/multilevel_index.csv')

# Write recipe outputs
test_multi = dataiku.Dataset("test_multi")
test_multi.write_with_schema(test_multi_df)
