import requests
import pandas as pd

headers = { 'AccountKey' : 'iPfmKlxrSvu9oLEmxJu2Jw==', 'accept' : 'application/json'}

# Obtain the url required for obtaining the data from the API
url = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"

# Convert the response/output into json
results = []

while True:
    new_results = requests.get(url, 
        headers=headers, 
        params={'$skip': len(results)}
    ).json()['value']
    
    if new_results == []:
        break
    else:
        results += new_results

Bus_service_df = pd.DataFrame(results)
Bus_service_df.to_excel("BusStopsList.xlsx")

