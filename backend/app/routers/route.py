from fastapi import APIRouter
from services import open_meteo


router = APIRouter()


@router.get("/search-city/:city")
def get_city(city:str):
    cities = open_meteo.get_list_city(city)
    return open_meteo.get_details_of_city(cities)


@router.get("/compares")
def hello_world(latitude:float, longitude:float, latitude2:float, longitude2:float):
    cities = [{"latitude": latitude, "longitude": longitude}, {"latitude": latitude2, "longitude": longitude2}]
    return open_meteo.get_details_of_city(cities)