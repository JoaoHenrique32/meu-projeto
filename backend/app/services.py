import httpx
from app.utils import retry_on_failure

PRIMARY_API_URL = "https://api.open-meteo.com/v1/forecast"
BACKUP_API_URL = "https://api.weatherapi.com/v1/current.json"
WEATHERAPI_KEY = "e610b76919aa41d29c5215108242611"

@retry_on_failure
async def fetch_weather_data(location: str):
    async with httpx.AsyncClient() as client:
        try:
            # Primeira tentativa com a API principal
            response = await client.get(
                PRIMARY_API_URL, params={"latitude": "0", "longitude": "0", "current_weather": "true"}
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            # Segunda tentativa com a API de backup
            response = await client.get(
                BACKUP_API_URL, params={"q": location, "key": WEATHERAPI_KEY}
            )
            response.raise_for_status()
            return response.json()
