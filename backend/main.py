from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

# Routers
logs_router = APIRouter()
alerts_router = APIRouter()
incidents_router = APIRouter()
rules_router = APIRouter()

# Example route in logs
@logs_router.get("/logs")
async def read_logs():
    return {"message": "Logs endpoint"}

# Example route in alerts
@alerts_router.get("/alerts")
async def read_alerts():
    return {"message": "Alerts endpoint"}

# Example route in incidents
@incidents_router.get("/incidents")
async def read_incidents():
    return {"message": "Incidents endpoint"}

# Example route in rules
@rules_router.get("/rules")
async def read_rules():
    return {"message": "Rules endpoint"}

# Including routers
app.include_router(logs_router, prefix="/logs")
app.include_router(alerts_router, prefix="/alerts")
app.include_router(incidents_router, prefix="/incidents")
app.include_router(rules_router, prefix="/rules")

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)