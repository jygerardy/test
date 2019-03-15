import dataiku,os.path,pyspark


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

te_df = ... # Compute a Pandas dataframe to write into te


# Write recipe outputs
te = dataiku.Dataset("te")
te.write_with_schema(te_df)
