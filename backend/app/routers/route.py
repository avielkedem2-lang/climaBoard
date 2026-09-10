from fastapi import APIRouter
from services import open_meteo
from schemas.schema_pydantic import DefinitionCity
from data.read_file import *


router = APIRouter()
@router.get("/health")
async def health():
    return "The server working"

@router.get("/search-city/:city")
async def get_city(city:str):
    cities = open_meteo.get_list_city(city)
    return open_meteo.get_details_of_city(cities)


@router.post("/favorite")
def favorite(body:DefinitionCity):
    favorites = read_file()
    favorites.append(body)
    write_file(favorites)
    return {"success": True}


@router.get("/compares")
async def compares(latitude:float, longitude:float, latitude2:float, longitude2:float):
    cities = [{"latitude": latitude, "longitude": longitude}, {"latitude": latitude2, "longitude": longitude2}]
    return open_meteo.get_details_of_city(cities)