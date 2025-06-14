from pydantic import BaseModel, HttpUrl
from datetime import datetime

class Policy(BaseModel):
    title: str
    description: str
    issued_date: datetime
    document_url: HttpUrl

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Solar Rooftop Subsidy Policy",
                "description": "Subsidies up to 40% on installation of residential solar rooftop systems.",
                "issued_date": "2024-07-15T00:00:00",
                "document_url": "http://localhost:8000/static/documents/solar_policy.pdf"
            }
        }

class PolicyResponse(BaseModel):
    policy_name: str
    summary: str

    class Config:
        json_schema_extra = {
            "example": {
                "policy_name": "Smart City Energy Plan",
                "summary": "Reduce city emissions by 25% by 2027."
            }
        }

class PolicyListResponse(BaseModel):
    policies: list[PolicyResponse]

    class Config:
        json_schema_extra = {
            "example": {
                "policies": [
                    {"policy_name": "Smart City Energy Plan", "summary": "Reduce city emissions by 25% by 2027."},
                    {"policy_name": "Waste Management Act", "summary": "Mandatory recycling and green bins in all households."}
                ]
            }
        }

class PolicyDetailResponse(PolicyResponse):
    description: str
    issued_date: datetime
    document_url: HttpUrl

    class Config:
        json_schema_extra = {
            "example": {
                "policy_name": "Smart City Energy Plan",
                "summary": "Reduce city emissions by 25% by 2027.",
                "description": "This policy aims to implement various measures to reduce carbon emissions in urban areas.",
                "issued_date": "2024-07-15T00:00:00",
                "document_url": "http://localhost:8000/static/documents/smart_city_energy_plan.pdf"
            }
        }
