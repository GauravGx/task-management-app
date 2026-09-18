from fastapi import APIRouter, HTTPException, status,Depends
from app.schemas.task_datastructure import taskCreate, TaskUpdate, TaskResponse
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.models.tasks_model import Task


router = APIRouter()





# database session cheks

@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
     return {"message": "Database session connected successfully"}

# view API
@router.get("/tasks",response_model = list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()



# view API by Id
@router.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id: int,db: Session = Depends(get_db)):
     #yato record ajayega ya None ayega
     task = db.query(Task).filter(Task.id == task_id).first()

     if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
         )

     return task



#insert data API

@router.post("/tasks",response_model = TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(task : taskCreate,db: Session = Depends(get_db)):
     print(task) #json data
     new_task = Task(  # but this is object of SQLAlchemy model
          title = task.title,
          description = task.description,
          is_completed = False
     )
    #  tasks.append(new_task)
     db.add(new_task)
     db.commit()
     db.refresh(new_task)
     return new_task   



#update API

@router.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(task_id: int,task: TaskUpdate, db: Session = Depends(get_db)):

    existing_task =  db.query(Task).filter(Task.id == task_id).first()
     
    if existing_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.is_completed = task.is_completed

    db.commit()
    db.refresh(existing_task)
    return existing_task
    
      
      
      



#delete API

@router.delete("/tasks/{task_id}")
def delete_task(task_id : int , db : Session=Depends(get_db)):
     task = db.query(Task).filter(Task.id == task_id).first()

     if task is None:
         raise HTTPException(
             status_code = status.HTTP_404_NOT_FOUND,
             detail = "Task not Found"
         ) 

     db.delete(task)
     db.commit()
     return {"message": "Task deleted successfully"
             }
    