import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()
API_KEY = os.getenv('OPENROUTE_API')

def getLatLong(address):
    url = f"https://api.openrouteservice.org/geocode/search?api_key={API_KEY}&text={address}"
    response = requests.get(url)
    data = response.json()
    return data["features"][0]["geometry"]["coordinates"]
def getAPIDuration(startAddress, endAddress):
    start_coords = getLatLong(startAddress)
    end_coords = getLatLong(endAddress)
    
    url = "https://api.openrouteservice.org/v2/directions/driving-car/json"
    headers = {"Authorization": API_KEY, "Content-Type": "application/json"}
    body = {
        "coordinates": [start_coords, end_coords],
        "instructions": False
    }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()

    # print(json.dumps(data, indent = 4))
    time = (data["routes"][0]["summary"]["duration"])/60
    # print(f"Time is {time} and type is {type(time)}")
    return round(time)

# a = getAPIDuration()
# print(a)
