from pydantic import BaseModel, Field, field_validator

# Client se aane aur client ko jaane wale data ka structure
# simple sabdo me kis formate me data ayega aor kis formate me data jayega.
# Schema = API data ka contract.(Data Validation)

# task creation
class taskCreate(BaseModel): # automatically 422 Unprocessable Entity response dega
      title: str = Field(min_length=3,max_length=500)
      description : str = Field(min_length =3,max_length =500)
      user_id: int
      @field_validator('title','description')
      @classmethod
      def validate_text(cls,value):
            value = value.strip()


            if not value:
                  raise ValueError("Value cannot be emty")

            return value
# Response model 
class TaskResponse(BaseModel):
        id : int
        title: str
        description: str
        is_completed : bool
        user_id: int

#Update Model
class TaskUpdate(BaseModel):
     title: str =Field(
        min_length=3,
        max_length=100
    )
     description: str =Field(
        min_length=3,
        max_length=500
    )
     is_completed:bool

     @field_validator("title", "description")
     @classmethod
     def validate_text(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Value cannot be empty")

        return value

