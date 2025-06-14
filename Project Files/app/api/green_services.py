from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Service(BaseModel):
    name: str
    type: str
    location: str
    latitude: float
    longitude: float

services = [
    {
        "name": "EV Charging Station - Jubilee Hills",
        "type": "EV Charging Station",
        "location": "Jubilee Hills, Hyderabad",
        "latitude": 17.4239,
        "longitude": 78.4111
    },
    {
        "name": "KBR National Park",
        "type": "Park",
        "location": "KBR Park Road, Hyderabad",
        "latitude": 17.4156,
        "longitude": 78.4275
    },
    {
        "name": "Recycling Center - Banjara Hills",
        "type": "Recycling Center",
        "location": "Banjara Hills, Hyderabad",
        "latitude": 17.4123,
        "longitude": 78.4411
    }
]

@router.get("/services/list", response_model=List[Service])
def list_services():
    return services
