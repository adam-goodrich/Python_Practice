import requests

response = requests.get("http://api.giphy.com/v1/gifs/search?q=anal+cavity&api_key=dc6zaTOxFJmzC")
good_boi = response.json()

for i in good_boi["data"]:
	print(i["url"])