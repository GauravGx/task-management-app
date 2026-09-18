from pydantic import BaseModel

# Client se aane aur client ko jaane wale data ka structure
# simple sabdo me kis formate me data ayega aor kis formate me data jayega.
# Schema = API data ka contract.

# task creation
class taskCreate(BaseModel):
      title: str
      description : str

# Response model 
class TaskResponse(BaseModel):
        id : int
        title: str
        description: str
        is_completed : bool

#Update Model
class TaskUpdate(BaseModel):
     title: str
     description: str
     is_completed:bool