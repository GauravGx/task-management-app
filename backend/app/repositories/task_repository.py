# this repo is responcible for data base communtioatio only not bussiness logic
from sqlalchemy.orm import Session  # database session chalane aor close ke liye
from app.models.tasks_model import Task  # hamara database model

# Repository: Database operation handle karta hai.



# get_all_tasks()
#       ↓
# SQLAlchemy
#       ↓
# SELECT * FROM tasks
#       ↓
# PostgreSQL

# ye method ka kaam database se sare record leke ane ka hai

def get_all_tasks(db: Session):
    return db.query(Task).all()

#single data ke liye

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

#new data store karne ke liye
def create_task(db: Session, task: Task): # yaha data jo arha hai wo Task Table model hai jo backend me define hai
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


#update data ke  leye
#yaha me task ke ander existing task hao ao aor jo titile,deccription and bool wo frontend se arha hai update ke liye
def update_task( db: Session, task: Task, title: str, description: str, is_completed: bool  ):
    task.title = title
    task.description = description
    task.is_completed = is_completed

    db.commit()
    db.refresh(task)

    return task


#delete data operation
def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
    return {"message": "deleted Successfully"}



def get_task_by_user(db:Session,user_id:int):
     return db.query(Task).filter(Task.user_id ==user_id).all()

# def get_tasks_with_pagination(db: Session, skip: int, limit: int):
#     return (
#         db.query(Task)
#         .order_by(Task.id.desc())
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )

# sort data with pagination and filter
def get_tasks_with_pagination(db: Session, skip: int, limit: int,sort:str):
         query = db.query(Task)
         if sort =="latest":
              query = query.order_by(Task.id.desc())
         elif sort == "oldest":
              query = query.order_by(Task.id.asc())     
         return (
                   query.offset(skip)
                   .limit(limit)
                   .all()
               )





# sort data with pagination with user id and filter
def get_tasks_by_user_with_pagination(
    db: Session,
    user_id: int,
    skip: int,
    limit: int,
    sort : str
):

    query = db.query(Task).filter(Task.user_id == user_id)
    if sort == "latest":
         query = query.order_by(Task.id.desc())
    elif sort == "oldest":
         query == query.order_by(Task.id.asc())

    return (
        
          query
          .offset(skip)
          .limit(limit)
          .all()
    )



# Searching Technique
def search_task(db: Session , search : str):
     return db.query(Task).filter(Task.title.ilike(f"%{search}%")).all()


# advance searching

def get_tasks_with_filters(
    db: Session,
    user_id: int | None,
    search: str | None,
    is_completed: bool | None,
    skip: int,
    limit: int,
    sort: str,
    
):
    query = db.query(Task)
    # 1 . user filter
    if user_id is not None: # collection of user task
        query = query.filter(Task.user_id == user_id)
    # 2. Search
    if search is not None: # filter data on collected using search key
        query = query.filter(
            Task.title.ilike(f"%{search}%")
        )
    # 3. Completed / Incomplete filter 
    if is_completed is not None:
        query = query.filter(
            Task.is_completed == is_completed
        )

     # 4 . Shorting data   
    if sort == "latest": # if latest to latest data
        query = query.order_by(Task.id.desc())

    elif sort == "oldest": # if oldest to oldest data
        query = query.order_by(Task.id.asc())

    
   # Pagination
    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )