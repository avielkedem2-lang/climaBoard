import { create } from "zustand";


type Current = {
    temperature_2m: number,
    wind_speed_10m: number,
    weather_code: number,
    apparent_temperature: number
}

type Daily = {
    temperature_2m_mean: number[],
    apparent_temperature_mean: number[],
    wind_speed_10m_max: number[],
    weather_code: number[]
}

type City = {
    current: Current,
    daily: Daily
}

type CityType = {
    cities: City[]
    setCities: (cities: City[]) => void
}



export const useCity = create<CityType>((set) => ({
    cities: [],
    setCities: (cities: City[]) => set(() => ({cities}))
}))