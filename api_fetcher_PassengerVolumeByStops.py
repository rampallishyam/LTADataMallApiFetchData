import requests
import pandas as pd

headers = { 'AccountKey' : 'iPfmKlxrSvu9oLEmxJu2Jw==', 'accept' : 'application/json'}

# Obtain the url required for obtaining the data from the API
url = "http://datamall2.mytransport.sg/ltaodataservice/PV/Bus"
# Write a code to obtain the data from the url 
response = requests.get(url,headers=headers, params={"$Date":202106}).json()
# Convert the response/output into json
#results = []
Bus_ped_data = pd.read_csv("transport_node_bus_202108.csv")
Bus_ped_data = Bus_ped_data.sort_values(by=['PT_CODE','DAY_TYPE','TIME_PER_HOUR'])
Bus_ped_data.to_csv("PassengerVOlumeByStops.csv")

# Code written for VROW

Bus_stop_code_list = [28091]
Bus_ped_data = pd.read_csv("PassengerVOlumeByStops.csv")
VROW_df = Bus_ped_data[Bus_ped_data['PT_CODE'].isin(Bus_stop_code_list)]
VROW_df.to_excel('PassengerVolumeByStopsLorAhSoo.xlsx')
