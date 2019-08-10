
# coding: utf-8

# In[23]:


import requests
import time
import csv


# In[24]:


r=requests.get("https://platform.tier-services.io/vehicle?zoneId=OSLO", headers={"X-Api-Key":"bpEUTJEBTf74oGRWxaIcW7aeZMzDDODe1yBoSxi2"})


# In[30]:


file_path = "../raw-data/tier_data" + str(int(time.time())) + ".csv"
f = csv.writer(open(file_path, "a+"))
data = r.json()['data']
print("Fetched data at time: " + str(time.time()))

for scooter in data:
    f.writerow([scooter["batteryLevel"],
                scooter["code"],
                scooter["iotVendor"],
                scooter["isRentable"],
                scooter["lastLocationUpdate"],
                scooter["lastStateChange"],
                scooter["lat"],
                scooter["licencePlate"],
                scooter["lng"],
                scooter["maxSpeed"],
                scooter["state"],
                scooter["vin"],
                scooter["zoneId"],
                int(time.time())])

