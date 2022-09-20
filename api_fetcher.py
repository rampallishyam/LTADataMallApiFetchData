import json
import requests

# 
headers = { 'AccountKey' : 'iPfmKlxrSvu9oLEmxJu2Jw==', 'accept' : 'application/json'}

# Obtain the url required for obtaining the data from the API
url = "http://datamall2.mytransport.sg/ltaodataservice/BusStops"
# Write a code to obtain the data from the url 
response = requests.get(url,headers=headers,params={'$skip': 50})
# # Convert the response/output into json
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

