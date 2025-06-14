from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from app.api import assistant, dashboard, alerts, policy,green_services
from app.api.assistant import generate_answer
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware # your assistant router

app = FastAPI()
load_dotenv()

app = FastAPI(
    title="Eco Visioner",
    description="An AI-powered assistant for sustainable city services",
    version="1.0.0"
)
# 🔐 Add SessionMiddleware with a secret key
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

# API Routers
app.include_router(assistant.router, prefix="/api/assistant", tags=["Assistant"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(policy.router, prefix="/api/policy", tags=["Policy"])
app.include_router(green_services.router, prefix="/api/green_services", tags=["Green Services"])


# Static + Templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Pages
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

@app.get("/assistant")
def assistant_page(request: Request):
    return templates.TemplateResponse("assistant.html", {"request": request, "title": "Ask Assistant"})

@app.post("/assistant")
def submit_question(request: Request, question: str = Form(...)):
    answer = generate_answer(question)
    return templates.TemplateResponse(
        "assistant.html",
        {
            "request": request,
            "title": "Ask Assistant",
            "answer": answer,
            "question": question
        }
    )

@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Dashboard"})

@app.get("/green_services")
def green_services_page(request: Request):
    return templates.TemplateResponse("green_services.html", {"request": request, "title": "Green Service Finder"})

@app.get("/alerts")
def alerts_page(request: Request):
    return templates.TemplateResponse("alerts.html", {"request": request, "title": "Alerts"})

@app.get("/policy")
def policy_page(request: Request):
    return templates.TemplateResponse("policy.html", {"request": request, "title": "Policies"})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("app/static/favicon.ico")
