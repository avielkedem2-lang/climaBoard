import requests

city = "paris"

res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
data = res.json()





def get_direction():
    return {"latitude": data["results"][0]["latitude"], "longitude": data["results"][0]["longitude"]}


direction = get_direction()
res1 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={direction["latitude"]}&longitude={direction["longitude"]}&current=temperature_2m,wind_speed_10m,weather_code,apparent_temperature&daily=temperature_2m_mean,apparent_temperature_mean,wind_speed_10m_max,weather_code&forecast_days=16")

data1 = res1.json()
