import axios from "axios";
import { useEffect, useState } from "react";



export function useFetch(url: string) {
    const [data, setData] = useState()

    useEffect(() => {
        const getResponse = async () => {
            const { data } = await axios.get(url);
            setData(data)
        }
    getResponse()
    },[url])

    return [data, setData]
}