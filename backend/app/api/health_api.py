
from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db


router1 = APIRouter()
@router1.get("/health")
def health_check(db: Session = Depends(get_db)):
  try:
      db.execute(text("SELECT 1"))
      return { "status":"healthy",
              "database":"connected"
              }
  except Exception:
          return { "status": "unhealthy",
                  "database":"disconnected"}

# database session cheks
@router1.get("/db-test")
def db_test(db: Session = Depends(get_db)):
     return {"message": "Database session connected successfully"}
