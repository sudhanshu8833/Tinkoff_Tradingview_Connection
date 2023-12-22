import requests
import pandas as pd
import json
def this_scripts():
    
    url="https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"

    data=requests.get(url=url)

    data=data.json()
    df = pd.DataFrame(data)
    tokens=df.set_index('symbol')['token'].to_dict()

    json_file_path = 'token.json'

    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(tokens, json_file)

this_scripts()