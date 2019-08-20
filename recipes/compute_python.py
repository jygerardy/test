# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
_in = dataiku.Dataset("distinct_prepared")
_out = dataiku.Dataset("python")

schema_in = _in.read_schema()
repr(schema_in)

_out.write_schema(schema_in)


with _out.get_writer() as writer:
    for d in _in.iter_rows():
        writer.write_row_dict(d)