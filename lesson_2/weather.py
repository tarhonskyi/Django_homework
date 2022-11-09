from requests import get

key = "1d242ecc98d0b69902977b69f733bdb0"  # GET IT FROM https://home.openweathermap.org/api_keys


def get_weather_info(city: str):
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}'
    response = get(weather_api).json()
    return response


if __name__ == "__main__":
    your_city = "aasd"
    city_weather = get_weather_info(your_city)
    print(city_weather)
    your_city = "Korosten"
    city_weather = get_weather_info(your_city)
    print(city_weather)

