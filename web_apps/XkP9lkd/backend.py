import dataiku
import pandas as pd
import dataikuapi
from datetime import datetime



# Example:
# From JavaScript, you can access the defined endpoints using
# getWebAppBackendUrl('first_api_call')

auto_hostname = 'http://localhost:30500'
auto_api_key = 'tGrJvlIQZDRjLnOq5DrftqWUs1UMxCYC'

client_auto = dataikuapi.DSSClient(auto_hostname, auto_api_key)
client_design = dataiku.api_client()
project_design = client_design.get_project(project)
project_auto = client_auto.get_project(project)


def list_bundles(bundles):
    return


def create_bundle():
    name = str(datetime.now())
    project_design.export_bundle(name)
    



@app.route('/first_api_call')
def first_call():
    mydataset = dataiku.Dataset("REPLACE_WITH_YOUR_DATASET_NAME")
    mydataset_df = mydataset.get_dataframe(sampling='head', limit=500)

    #Pandas dataFrames are not directly JSON serializable, use to_json()
    data = mydataset_df.to_json()
    return json.dumps({"status": "ok", "data": data})


@app.route('/list_bundles')
def list_bundles():
    project = dataiku.get_custom_variables().get('projectKey')
    if project not in client_auto.list_projects()
        return json.dumps({"status": "missing_auto_project"})
    else:
        project_design = client_design.get_project(project)
        project_auto = client_auto.get_project(project)
        bundles_auto = project_auto.list_importe
    
    