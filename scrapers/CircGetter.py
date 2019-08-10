
# coding: utf-8

# In[41]:


import requests
import time
import csv
import pandas as pd
from pathlib import Path


# In[58]:


print("Fetched data at time: " + str(time.time()))


# In[52]:


tim = int(time.time())


# In[49]:


coords = [[59.914091, 10.737777],
[59.911079, 10.726607],
[59.918312, 10.710500],
[59.930118, 10.697486],
[59.939106, 10.713644],
[59.941212, 10.758963],
[59.930893, 10.758619],
[59.918892, 10.785742],
[59.912352, 10.771923],
[59.912084,10.749457],
[59.907964,10.740960],
[59.919654,10.717954]]


# In[65]:


def get_scooters(lat, long):
    r=requests.get("https://api.goflash.com/api/Mobile/Scooters?userLatitude="+lat+"&userLongitude="+long+"&lang=en&latitude="+lat+"&longitude="+long+"&latitudeDelta=0.10&longitudeDelta=0.05")
    data = r.json()['Data']['Scooters']
    res = []
    for scooter in data:
        res.append([scooter["idScooter"],
                    scooter["Distance"],
                    scooter["IsBookable"],
                    scooter["PowerPercentInt"],
                    scooter['LatLng']['_geometry']['m_points'][0]['x'],
                    scooter['LatLng']['_geometry']['m_points'][0]['y'],
                    scooter["RemainderRange"],
                    scooter["ScooterModel"],
                    scooter["idScooterState"],
                    scooter["txt_Code"],
                    tim])
    return pd.DataFrame(res)


# In[66]:


dfs = []
for coord in coords:
    df = get_scooters(str(coord[0]), str(coord[1]))
    dfs.append(df)
df = pd.concat(dfs, axis =0)


# In[68]:


df = df.drop_duplicates(subset=[0])


# In[71]:

file_path = str(Path().resolve().parent) + "/raw-data/tier_data" + ".csv"

with open(file_path, 'a+') as f:
    df.to_csv(f, header=False)

