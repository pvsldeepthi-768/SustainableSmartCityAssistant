from pydantic import BaseModel

class DashboardMetrics(BaseModel):
    carbon_emissions: float
    energy_usage: float
    recycling_rate: float
