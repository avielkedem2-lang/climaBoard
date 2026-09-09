from fastapi import APIRouter
from services import open_meteo


router = APIRouter()


@router.get("/search-city/:city")
def get_city(city:str):
    return


@router.get("/")
def hello_world():
    data1 = open_meteo.data1
    # data = api_services.data
    return data1