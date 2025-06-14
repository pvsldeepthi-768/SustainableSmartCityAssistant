# app/schemas/alert_schemas.py

from pydantic import BaseModel, HttpUrl
from datetime import datetime

class Alert(BaseModel):
    id: int
    title: str
    description: str
    type: str  # e.g. "activity", "program", "emergency"
    timestamp: datetime
    image_url: HttpUrl

class AlertResponse(BaseModel):
    alerts: list[Alert]
