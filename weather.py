import requests

API_key = "49e50c7f6549a11b5a2d91fbb394091c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
URL_request = f"{BASE_URL}?appid={API_key}&q={city}"

response = requests.get(URL_request)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 2)

    print(f"Weather: {weather}")
    print(f"Temperature: {temp}°C")
else:
    print("Error in the HTTP request")
