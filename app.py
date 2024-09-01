import requests

api_key = 'da173b4d54309e634055b00da5e4af25'

user_input = input("Enter City Name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code == 404:
    print("No City Found")
else:
    weather_json = weather_data.json()
    weather = weather_json['weather'][0]['main']
    temp = round(weather_json['main']['temp'])
    feels_like = round(weather_json['main']['feels_like'])
    temp_min = round(weather_json['main']['temp_min'])
    temp_max = round(weather_json['main']['temp_max'])
    humidity = weather_json['main']['humidity']
    wind_speed = weather_json['wind']['speed']
    visibility = weather_json['visibility']
    sunrise = weather_json['sys']['sunrise']
    sunset = weather_json['sys']['sunset']

    print(f"Weather in {weather_json['name']}: {weather}")
    print(f"Temperature: {temp}ºF")
    print(f"Feels Like: {feels_like}ºF")
    print(f"Min Temperature: {temp_min}ºF")
    print(f"Max Temperature: {temp_max}ºF")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Visibility: {visibility} meters")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")



