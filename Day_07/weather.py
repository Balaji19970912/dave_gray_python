import requests
from pprint import pprint
# from dotenv import load_dotenv
# import os

# load_dotenv()

def get_current_weather():
    API_KEY = "e7a1dff521067816c1e07c65da5b6024"
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: \n")

    try:
        request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&q={city}&units=imperial"

        weather_data = requests.get(request_url).json()

        # print(request_url)
        # pprint(weather_data)

        current_temperature = (weather_data["main"]["temp"] - 32)*(5/9)
        maximum_temperature = (weather_data["main"]["temp_max"] - 32)*(5/9)
        minimum_temperature = (weather_data["main"]["temp_min"] - 32)*(5/9)
        print(f"\nCurrent temperature is : {current_temperature:.2f} degree celcius")
        print(f"\nToday's Maximum temperature is : {maximum_temperature:.2f} degree celcius")
        print(f"\nToday's Minimum temperature is : {minimum_temperature:.2f} degree celcius\n")
    
    except:
        print("\nInvalid input!\n")


get_current_weather()