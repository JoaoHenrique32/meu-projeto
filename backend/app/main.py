from fastapi import FastAPI, HTTPException
from app.services import fetch_weather_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}

@app.get("/weather/")
async def get_weather(location: str):
    try:
        # Consulta à API do tempo
        data = await fetch_weather_data(location)
        return {"location": location, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
