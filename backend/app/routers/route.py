from fastapi import APIRouter
from services import open_meteo


router = APIRouter()


@router.get("/search-city/:city")
def get_city(city:str):
    cities = open_meteo.get_list_city(city)
    return open_meteo.get_details_of_city(cities)


# @router.get("/compares")
# def hello_world():
#     data1 = open_meteo.data1
#     return data1