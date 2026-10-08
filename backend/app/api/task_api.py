from fastapi import APIRouter, HTTPException, status,Depends
from app.schemas.task_datastructure import taskCreate, TaskUpdate, TaskResponse
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.services.task_service import create_task_service, delete_task_by_id_service, get_task_by_id_service, get_task_service, get_tasks_by_user_with_pagination_service, get_tasks_with_filters_service, get_tasks_with_pagination_service, search_tasks_service, update_task_service
import logging


#bassically ye turminal me proper resion ke saath output dega kya problem hui hai ya kya process hui hai

logger = logging.getLogger(__name__)


# Router: HTTP request aur response handle karta hai.
router = APIRouter()







# view All data API
# @router.get("/tasks",response_model = list[TaskResponse])
# def get_task_endpoint(db: Session = Depends(get_db)):
#     return get_task_service(db)

# @router.get("/tasks",response_model = list[TaskResponse])
# def get_task_endpoint(skip: int = 0,limit: int=10,db: Session = Depends(get_db)):
#           if skip< 0:
#             skip = 0

#           if limit<=0:
#                limit=10

#           return get_tasks_with_pagination_service(db,skip,limit)      

@router.get("/tasks", response_model=list[TaskResponse])
def get_task_endpoint(
    user_id: int | None = None,
    search: str | None = None,
    is_completed: bool | None=None,
    skip: int = 0,
    limit: int = 10,
    sort: str = "latest",
    db: Session = Depends(get_db)
):
    if skip < 0:
        skip = 0

    if limit <= 0:
        limit = 10

    if sort not in ["latest", "oldest"]:
        sort = "latest"

    return get_tasks_with_filters_service(
        db,
        user_id,
        search,
        is_completed,
        skip,
        limit,
        sort
    )
   

   



# view single data by Id Api
@router.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id: int,db: Session = Depends(get_db)):
     
     logger.info(f"Fetching task with id={task_id}")
     #yato record ajayega ya None ayega
     task = get_task_by_id_service(db,task_id)  # this function of Service operation repo

     if task is None:
        logger.warning(f"Task not found with id={task_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
         )

     return task



#insert new data API

@router.post("/tasks",response_model = TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task : taskCreate,db: Session = Depends(get_db)):
     logger.info(f"Creating task for user_id={task.user_id}")

     try:
          return create_task_service(db,task) #yaha new_task ka pydantic validation hoga fir objet pass hoga
     except Exception:
         logger.exception("Unexpected Error While creating Task")
         raise


#update API

@router.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task_endpoint(task_id: int,task: TaskUpdate, db: Session = Depends(get_db)):

    is_task = update_task_service(db,task_id,task)
    logger.info(f"Updating task with id={task_id}")
    if is_task is None:
        logger.warning(f"Cannot update. Task not found with id={task_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return is_task
    

    
      
      
#delete API

@router.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id : int , db : Session=Depends(get_db)):
     task = delete_task_by_id_service(db,task_id)
     logger.info(f"Deleting task with id={task_id}")
     if task is None:
         logger.warning(f"Cannot delete. Task not found with id={task_id}")
         raise HTTPException(
             status_code = status.HTTP_404_NOT_FOUND,
             detail = "Task not Found"
         ) 
    
     return task
    