import requests
from pprint import pprint
# from dotenv import load_dotenv
# import os

# load_dotenv()

def get_current_weather(city="Hosapete"):
    API_KEY = "e7a1dff521067816c1e07c65da5b6024"
   

    try:
        request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&q={city}&units=imperial"

        weather_data = requests.get(request_url).json()

        return weather_data
    
    except:
        print("\nInvalid input!\n")

if __name__ == "__main__" :
     print('\n*** Get Current Weather Conditions ***\n')
     city = input("\nPlease enter a city name: \n")
     pprint(get_current_weather(city))
     print("\n")