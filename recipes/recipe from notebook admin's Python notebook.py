# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import graphviz
print(graphviz.__version__)


dot_data = 'digraph {A->B}'
graph = graphviz.Source(dot_data)
graph.render('/Users/jygerardy/Desktop//dot_data', format='pdf', cleanup=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
client = dataiku.api_client()
project = client.get_project('PLUGINS_DEV')
project.list_recipes()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dataset_names = [dataset.get('name') for dataset in t.list_datasets()]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for ds in dataset_names:
    dataset = t.get_dataset(ds)
    x = dataset.get_definition()
    for i in x:
        print (x)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
dataset = dataiku.Dataset('companylist')

df = dataset.get_dataframe(infer_with_pandas=False)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from dataiku.fsprovider import FSProvider

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for k, v in os.environ.iteritems():
    print(k,v)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fsp = FSProvider()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # SQL code extractor
# 
# ## Overview
# * One of the strengths of DSS is its ability to run <b>visual recipes</b> using the engine where the data is stored. https://www.dataiku.com/learn/guide/getting-started/dss-concepts/where-does-it-all-happen.html
# 
# * To that end, DSS translates visual recipes into code that can then be pushed down to the data source.
# 
# * Among all the different translation options, there are SQL(-like) languages such as tradional SQL on tradional relational databases (Postgres, MySQL , Oracle etc.)  but also Hive, Impala and SparkSQL on Hadoop clusters.
# 
# * DSS users can also directly write <b>code recipes</b> in those languages.
# 
# * The goal of this Macro is to extract SQL codes from those (visual and code) recipes in either the project in which one executes the Macro or across all projects in the instance.
# 
# ## Usage
# 
# ### Input
# * This macros takes as input an existing <b>filesystem</b> folder in the project where the macro is used. This folder cannot be on a remote FS (S3...)
# * The user can choose to either run the macro on the current project or across all the project they have access to on the isntance
# 
# ### Output
# * The output is zip file dumped in the chosen folder and a report table that shows the count of recipes per recipes from which SQL code was retrieved.
# 
# * The structure in the zipped folder is sql_extract-{extractionTime}/{projeckKey}/{recipeName.sql}
# 
# 
# 
# ### Limitations
# 
# * This Macro is unable to retrieve SQL from the following visual recipes: pivot, distinct, topn, groupby, window
# 
# 
# * This Macro will parse all the recipes in either the project in which one runs the Macro or across all projects in the instance to retrieve all SQL code generated
# 
# 
# # License
# 
# Apache Software License

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
OK: join, stack, pivot, sample
NOK: pivot, distinct, topn, groupby, window

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
client._perform_json(
"GET", "/projects/%s/recipes/%s/status" % ('PLUGINS_DEV', 'compute_distinct'))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku

client = dataiku.api_client()


project = client.get_project('PLUGINS_DEV')
rec = project.get_recipe('compute_sample')

dap = rec.get_definition_and_payload()
status = rec.get_status()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
print(status.data.get('sql'))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
status.data.get('sql')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dap.get_payload()