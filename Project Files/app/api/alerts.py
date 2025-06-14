# app/api/alerts.py

from fastapi import APIRouter
from typing import List
from app.schemas.alerts_schemas import Alert
import datetime

router = APIRouter()

# Sample alert data source simulation
sample_alerts = [
    {
        "id": 1,
        "title": "New Solar Rooftop Program Launched",
        "description": "City government initiates solar rooftop installations to boost green energy adoption.",
        "type": "program",
        "timestamp": datetime.datetime.now() - datetime.timedelta(minutes=10),
        "image_url":"http://localhost:8000/static/images/alerts/SolarRooftopEnergy.jpg"
    },
    {
        "id": 2,
        "title": "Heavy Rain Warning - Flood Risk",
        "description": "Meteorological department issues heavy rain warning for low-lying areas. Citizens advised to stay alert.",
        "type": "emergency",
        "timestamp": datetime.datetime.now() - datetime.timedelta(minutes=5),
        "image_url": "http://localhost:8000/static/images/alerts/Heavy-Rain-alert.png"
    },
    {
        "id": 3,
        "title": "Community Clean-up Drive This Weekend",
        "description": "Join the city-wide clean-up drive to improve local parks and neighborhoods.",
        "type": "activity",
        "timestamp": datetime.datetime.now() - datetime.timedelta(hours=1),
        "image_url": "http://localhost:8000/static/images/alerts/CleanCity.jpeg"
    },
    {
        "id": 4,
        "title": "Air Quality Alert: High Pollution Levels",
        "description": "Due to increased vehicular emissions, the AQI has reached hazardous levels. Use masks outdoors.",
        "type": "emergency",
        "timestamp": datetime.datetime.now() - datetime.timedelta(minutes=30),
        "image_url": "http://localhost:8000/static/images/alerts/AirQuality.webp"
    },
]

@router.get("/alerts", response_model=List[Alert])
async def get_alerts():
    # Simulate real-time alerts by shuffling and limiting to top 5 latest
    alerts_sorted = sorted(sample_alerts, key=lambda x: x["timestamp"], reverse=True)
    # You could add new alerts dynamically here or fetch from DB
    return alerts_sorted[:5]
