from dataiku.customwebapp import *
import dataiku
from flask import request
import json
import requests
import copy




endpoint = get_webapp_config().get("endpoint")
apikey = get_webapp_config().get("apikey")

def generate_grid(selected_var, features_json, counter_factuals):
    grid = {"items": []}
    for cf in counter_factuals:
        new_features_json = copy.deepcopy(features_json)
        new_features_json[selected_var] = cf
        grid["items"].append(new_features_json)
    return grid
        
        

# need to score to make the API call from the backend to avoid CORS hell.
@app.route('/score')
def score():
    features_json = request.args.get("featuresJson")
    selected_variable = request.args.get("selectedVariable")
    counter_factuals = request.args.get("counterFactuals")
    
    
    
    
    print("Scoring grid:")
    print(grid)
    r = requests.post(endpoint, auth=(apikey, ''), data=grid)
    return json.dumps({"data": r.json()})
