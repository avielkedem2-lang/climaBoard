import requests

def get_list_city(city):
    res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    if (res.status_code != 200):
        return "error"
    data = res.json()
    cities = []
    for c in data["results"]:
        all_city = {"name": c["name"], "latitude": c["latitude"], "longitude": c["longitude"]}
        cities.append(all_city)
    
    return cities






def get_details_of_city(cities:list):
    cities_details = []
    for city in cities:
        res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={city["latitude"]}&longitude={city["longitude"]}&current=temperature_2m,wind_speed_10m,weather_code,apparent_temperature&daily=temperature_2m_mean,apparent_temperature_mean,wind_speed_10m_max,weather_code")
        data = res.json()
        city_detail = {"current": {
            "temperature_2m": data["current"]["temperature_2m"],
            "wind_speed_10m": data["current"]["wind_speed_10m"],
            "weather_code": data["current"]["weather_code"],
            "apparent_temperature": data["current"]["apparent_temperature"]
            },    
                       "daily": {
                           "temperature_2m_mean": data["daily"]["temperature_2m_mean"],
                           "apparent_temperature_mean": data["daily"]["apparent_temperature_mean"],
                           "wind_speed_10m_max": data["daily"]["wind_speed_10m_max"],
                           "weather_code": data["daily"]["weather_code"]
                                }}
        cities_details.append(city_detail)
    return cities_details
        
    






