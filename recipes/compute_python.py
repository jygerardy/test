# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
_in = dataiku.Dataset("distinct_prepared")
_out = dataiku.Dataset("python")

schema_in = _in.read_schema()
schema_out = [{u'type': u'string', u'name': u'Symbol'},
              {u'type': u'string', u'name': u'Name'},
              {u'type': u'string', u'name': u'LastSale'},
              {u'type': u'double', u'name': u'MarketCap'},
              {u'type': u'string', u'name': u'ADR TSO'},
              {u'type': u'string', u'name': u'IPOyear'},
              {u'type': u'string', u'name': u'Sector'},
              {u'type': u'string', u'name': u'Industry'},
              {u'type': u'string', u'name': u'Summary Quote'},
              {u'type': u'string', u'name': u'col_9'}
             ]

_out.write_schema(schema_out)


with _out.get_writer() as writer:
    for d in _in.iter_rows():
        writer.write_row_dict(d)