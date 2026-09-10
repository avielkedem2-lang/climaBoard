from pydantic import BaseModel, Field

class DefinitionCurrent(BaseModel):
    temperature_2m: int
    wind_speed_10m: int
    weather_code: int
    apparent_temperature: int
    
    


class DefinitionDaily(BaseModel):
    temperature_2m_mean: list[int]
    apparent_temperature_mean: list[int]
    wind_speed_10m_max: list[int]
    weather_code: list[int]





class DefinitionCity(BaseModel):
    current: DefinitionCurrent
    daily: DefinitionDaily