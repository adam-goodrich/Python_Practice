import requests

def get_weather():
    zip_code = input("what is your zip code? ")
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid=052f26926ae9784c2d677ca7bc5dec98")
    weather = response.json()
    change_weather = (weather["main"]["temp"])
    city = (weather["name"])
    to_fahrenheit = (((change_weather)-273.15) * 9/5 + 32)
    return((str(int(to_fahrenheit))) + " Degrees Fahrenheit is the tempature in " + city)

print(get_weather())