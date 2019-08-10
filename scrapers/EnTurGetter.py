import requests
import json
import csv
import time
from pathlib import Path

url = "https://api.entur.io/mobility/v1/scooters?lat=59.911491&lon=10.757933&range=25000&max=20000"
file_path = str(Path().resolve().parent) + "/raw-data/scooter_info" + ".csv"
f = csv.writer(open(file_path, "a+"))
r = requests.get(url = url)
data = r.json()
print("Fetched data at time: " + str(time.time()))

for scooter in data:
    f.writerow([scooter["id"],
                scooter["operator"],
                scooter["lat"],
                scooter["lon"],
                scooter["code"],
                scooter["battery"],
                int(time.time())])
