from sqlalchemy.orm import Session
from app.repositories.task_repository import create_task, delete_task, get_all_tasks, get_task_by_id, get_task_by_user, get_tasks_by_user_with_pagination, get_tasks_with_filters, get_tasks_with_pagination, search_task, update_task
from app.models.tasks_model import Task
from app.schemas.task_datastructure import TaskUpdate, taskCreate


#service for get all data from database and return it
def get_task_service(db : Session):
    return get_all_tasks(db)


#service for create Tasks

def create_task_service(db: Session,task_data:taskCreate):
         new_task = Task(  # but this is object of SQLAlchemy model
                  title = task_data.title,
                  description = task_data.description,
                  is_completed = False,
                  user_id=task_data.user_id
              )
         return create_task(db,new_task)



#service for update task

def update_task_service(db:Session,task_id:int,new_task:TaskUpdate):
       existing_task =  get_task_by_id(db,task_id)
       if existing_task is None:
        return None
       return update_task(db,existing_task,new_task.title,new_task.description,new_task.is_completed)


# service for get task by there task id
def get_task_by_id_service(db:Session,task_id:int):
       task = get_task_by_id(db,task_id) 
       return task


# service for delete task by there task id
def delete_task_by_id_service(db: Session,task_id:int):
       task = get_task_by_id(db,task_id)
       if task is None:
              return None
       return delete_task(db,task)


# service for get al
def get_tasks_by_user_service(db:Session,user_id:int):
      return get_task_by_user(db,user_id)


def get_tasks_with_pagination_service(
    db: Session,
    skip: int,
    limit: int,
    sort : str
):
    return get_tasks_with_pagination(db, skip, limit,sort)



def get_tasks_by_user_with_pagination_service(
    db: Session,
    user_id: int,
    skip: int,
    limit: int,
    sort : str
):
    return get_tasks_by_user_with_pagination(
        db,
        user_id,
        skip,
        limit,
        sort
    )


# search service

def search_tasks_service(db: Session,search:str):
      return search_task(db,search)

#advance search service

def get_tasks_with_filters_service(
    db: Session,
    user_id: int | None,
    search: str | None,
    is_completed: bool|None,
    skip: int,
    limit: int,
    sort: str
):
    return get_tasks_with_filters(
        db,
        user_id,
        search,
        is_completed,
        skip,
        limit,
        sort
    )