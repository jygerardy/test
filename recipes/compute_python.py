# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
distinct_prepared = dataiku.Dataset("distinct_prepared")
#distinct_prepared_df = distinct_prepared.get_dataframe()


py_recipe_output = dataiku.Dataset("python")
writer = py_recipe_output.get_writer()

# d is of the form :
#   {'col_0': value0, 'col_1': value1, ...}


for d in data_to_write:
    writer.write_row_dict(r)






# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.
