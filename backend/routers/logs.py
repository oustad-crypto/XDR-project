from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Model for log entries
class LogEntry(BaseModel):
    id: int
    message: str
    level: str  # e.g., INFO, ERROR
    timestamp: str  # e.g., '2026-03-28T15:50:00Z'

# In-memory log storage (you may want to replace this with a database in production)
logs = []

@router.post("/logs/ingest")
def ingest_log(log_entry: LogEntry):
    logs.append(log_entry.dict())  # Append the log entry
    return log_entry

@router.get("/logs/retrieve")
def retrieve_logs():
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found")
    return logs

