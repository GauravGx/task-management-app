from fastapi import FastAPI
from app.api.task_api import router as task_router
from app.api.health_api import router1 as task_router1
from app.models.user_model import User
from app.models.tasks_model import Task
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.core.logging_config import setup_logging

#create Fastapi app

app = FastAPI()

setup_logging()
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allowed from all origin
    allow_credentials=True,
    allow_methods=["*"],  # No condition Method
    allow_headers=["*"],  # all type header accepted
)





#Home route Responce
@app.get("/") # GET/ karega to niche wala function chalega
def home():
  return {"message": "Task Management API is running"}




# collection of CRUD routes
app.include_router(task_router)
# for Health cheks routes
app.include_router(task_router1)









  






