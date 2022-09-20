import requests
import pandas as pd

# 
headers = { 'AccountKey' : 'iPfmKlxrSvu9oLEmxJu2Jw==', 'accept' : 'application/json'}

# Obtain the url required for obtaining the data from the API
url = "http://datamall2.mytransport.sg/ltaodataservice/BusServices"
# Write a code to obtain the data from the url 
response = requests.get(url,headers=headers)
# # Convert the response/output into json
# data = response.json()

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

# Bus_services_list = [
# "3N", "1N", "14", "14A", "14e", "16", "16M", "106", "111", "131","162",
# "162M", "167", "175", "36", "36A", "36B", "652", "656", "660", "663", 
# "665", "77", "850E", "857", "951E", "971"
# ]

# Imp_bus_list = []
# for service in results:
#     if service['ServiceNo'] in Bus_services_list:
#         Imp_bus_list.append(service)

Bus_service_df = pd.DataFrame(results)
Bus_service_df.to_excel("Bus_services_list.xlsx")

