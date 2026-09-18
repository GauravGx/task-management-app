from fastapi import FastAPI
from app.api.task_api import router as task_router

#create Fastapi app

app = FastAPI()



#Home route Responce
@app.get("/") # GET/ karega to niche wala function chalega
def home():
    return {"message": "Task Management API is running"}


# collection of CRUD routes
app.include_router(task_router)










  






