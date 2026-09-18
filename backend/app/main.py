from fastapi import FastAPI,status,HTTPException
from app.api.task_api import router as task_router
from app.core.database import engine, Base
#create Fastapi app

app = FastAPI()

Base.metadata.create_all(bind=engine)


#Home route Responce
@app.get("/") # GET/ karega to niche wala function chalega
def home():
    return {"message": "Task Management API is running"}


# collection of CRUD routes
app.include_router(task_router)










  






