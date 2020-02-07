import geocoder

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
    print(f"{i} is located at ({lat}, {lon})")