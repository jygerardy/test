import dataiku
import pandas as pd
from flask import request

# Example:
# From JavaScript, you can access the defined endpoints using
# getWebAppBackendUrl('first_api_call')

@app.route('/first_api_call')
def first_call():
    print("X"*100)
    my_data = request.args.get('myData')
    print(my_data)

    return json.dumps({"status": "ok", "data": "whatever"})
