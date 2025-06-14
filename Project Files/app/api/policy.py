from fastapi import APIRouter
from app.schemas.policy_schemas import Policy, PolicyResponse, PolicyDetailResponse
from datetime import datetime

router = APIRouter()

# Mock in-memory DB for demo
policies = [
    {
        "policy_name": "Smart City Energy Plan",
        "summary": "Reduce city emissions by 25% by 2027.",
        "description": "This policy aims to implement measures for carbon reduction in urban areas.",
        "issued_date": "2024-07-15T00:00:00",
        "document_url": "http://localhost:8000/static/documents/smart_city_energy_plan.pdf"
    },
    {
        "policy_name": "Waste Management Act",
        "summary": "Mandatory recycling and green bins in all households.",
        "description": "Strict guidelines for segregating and processing waste.",
        "issued_date": "2023-05-22T00:00:00",
        "document_url": "http://localhost:8000/static/documents/waste_management_act.pdf"
    }
]

@router.get("/policies", response_model=list[PolicyResponse])
def get_policies():
    return [{"policy_name": p["policy_name"], "summary": p["summary"]} for p in policies]

@router.get("/policies/all-details")
def get_all_policies_full_details():
    return policies
