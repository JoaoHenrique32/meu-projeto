from fastapi import FastAPI, HTTPException
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

app = FastAPI()

API_PRIMARY = "https://api.openweathermap.org/data/2.5/weather"
API_BACKUP = "https://api.weatherapi.com/v1/current.json"
API_FORECAST_PRIMARY = "https://api.openweathermap.org/data/2.5/forecast"
API_FORECAST_BACKUP = "https://api.weatherapi.com/v1/forecast.json"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_data(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch data")
    return response.json()

@app.get("/current-temperature")
async def get_current_temperature(city: str):
    params = {"q": city, "appid": "2971f2fee32435787a6136e6e4bab0bf", "units": "metric"}
    try:
        data = fetch_data(API_PRIMARY, params)
        return {"temp": data["main"]["temp"]}
    except HTTPException:
        backup_params = {"key": "e610b76919aa41d29c5215108242611", "q": city}
        data = fetch_data(API_BACKUP, backup_params)
        return {"temp": data["current"]["temp_c"]}

@app.get("/forecast")
async def get_forecast(city: str):
    params = {"q": city, "appid": "2971f2fee32435787a6136e6e4bab0bf", "units": "metric", "cnt": 5}
    try:
        data = fetch_data(API_FORECAST_PRIMARY, params)
        forecast = [{"date": day["dt_txt"], "temp": day["main"]["temp"]} for day in data["list"]]
        return {"forecast": forecast}
    except HTTPException:
        backup_params = {"key": "e610b76919aa41d29c5215108242611", "q": city, "days": 5}
        data = fetch_data(API_FORECAST_BACKUP, backup_params)
        forecast = [{"date": day["date"], "temp": day["day"]["avgtemp_c"]} for day in data["forecast"]["forecastday"]]
        return {"forecast": forecast}
