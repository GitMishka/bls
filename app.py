import requests
import json
import pandas as pd
# BLS API test
headers = {"Content-type": "application/json"}

data = json.dumps({
    "seriesid": ['CES0500000003'], 
    "startyear":"2011", 
    "endyear":"2021",
    "registrationkey":"f5a17dddb91f40ac9e93c9ec8b9769a6" 
})

url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
response = requests.post(url, data=data, headers=headers)

if response.status_code == 200:
    result = json.loads(response.text)
    #print(json.dumps(result, indent=2))
else:
    print("Failed to retrieve data")

data_points = result['Results']['series'][0]['data']
df = pd.DataFrame(data_points)
print(df)

