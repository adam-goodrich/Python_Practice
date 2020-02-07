import geocoder
import requests

API_BASE_URL = "https://api.darksky.net/forecast/41634fad36d045146e519a22759fb576/"

location_list = ["Space Needle", 
"Crater Lake", 
"Golden Gate Bridge", 
"Yosemite National Park", 
"Las Vegas, Nevada", 
"Grand Canyon National Park", 
"Aspen, Colorado", 
"Mount Rushmore",
"Yellowstone National Park",
"Sandpoint, Idaho",
"Banff National Park",
"Capilano Suspension Bridge"]

for i in location_list:
    g = geocoder.arcgis(i)
    lat = g.latlng[0]
    lon = g.latlng[1]
    lat = round(lat, 4)
    lon = round(lon, 4)
    print(f"\n{i} is located at ({lat}, {lon})")
    full_api_url = (API_BASE_URL + str(lat) + "," + str(lon))
    result = requests.request('GET', full_api_url).json()
    condition = result['currently']['summary']
    temp = result['currently']['temperature']
    temp = round(temp, 1)
    degree = u"\u00B0" + "F"
    print(f"At {i} right now, it's {condition} with a temperature of {temp}{degree}\n")
  
  