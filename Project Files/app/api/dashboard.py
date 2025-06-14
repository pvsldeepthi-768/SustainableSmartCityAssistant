# app/api/dashboard.py

from fastapi import APIRouter
from typing import List
import httpx
import datetime

router = APIRouter()

# URLs for real data - only AQI is real API, others placeholders
OPENAQ_API_URL = "https://api.openaq.org/v2/latest?country=IN&limit=5"

async def fetch_aqi_highlights() -> List[str]:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(OPENAQ_API_URL)
        data = response.json()

        highlights = []
        now = datetime.datetime.now().strftime("%H:%M:%S")

        for location in data.get("results", []):
            city = location.get("city", "Unknown City")
            measurements = location.get("measurements", [])
            for measure in measurements:
                if measure["parameter"] == "pm25":
                    value = measure["value"]
                    unit = measure["unit"]
                    highlights.append(f"[{now}] PM2.5 level in {city} is {value} {unit} - Air Quality Indicator")
                    break  # Only one highlight per city

        return highlights[:3]

async def fetch_energy_data():
    # Simulate or extend to fetch from POSOCO or CEA API if available
    return {
        "current_load_gw": 180.5,
        "renewable_share_pct": 38.2,
        "peak_load_gw": 210.7
    }

async def fetch_water_usage():
    # Placeholder, could connect to NWIC or state portals
    return {
        "reservoir_level_pct": 72.4,
        "daily_usage_million_m3": 850,
        "smart_meter_coverage_pct": 45.0
    }

async def fetch_green_coverage():
    # Placeholder, could connect to FSI or ISRO Bhuvan
    return {
        "forest_cover_pct": 24.3,
        "urban_green_cover_pct": 15.6,
        "yearly_growth_pct": 1.2
    }

@router.get("/metrics")
async def get_dashboard_metrics():
    energy = await fetch_energy_data()
    water = await fetch_water_usage()
    green = await fetch_green_coverage()
    return {
        "energy": energy,
        "water": water,
        "green": green
    }

@router.get("/sustainable-highlights", response_model=List[str])
async def sustainable_highlights():
    try:
        aqi_highlights = await fetch_aqi_highlights()
    except Exception:
        aqi_highlights = ["Unable to fetch real-time AQI data currently."]
    # Simulated extra highlights (replace with real API calls as needed)
    now = datetime.datetime.now().strftime("%H:%M:%S")
    extra_highlights = [
        f"[{now}] India’s solar capacity crossed 50 GW, boosting clean energy.",
        f"[{now}] Maharashtra launches smart water meters for efficient usage.",
        f"[{now}] Forest Survey reports 1.2% increase in green cover this year."
    ]
    # Combine AQI + extra, pick 3 randomly for variety
    import random
    combined = aqi_highlights + extra_highlights
    return random.sample(combined, 3)
