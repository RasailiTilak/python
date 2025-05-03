from pydantic import BaseModel, Field#type:ignore
from typing import List, Dict, Optional
class User(BaseModel):
    id:int = 0 # default value
    name:str=Field(..., min_length=3,max_length=50,description="employee name", example="john doe") # default value
    is_active:bool=False # default value
    
    items: List[str] = [] # default value
    
    departments:Optional[str]='general' # default value
    salary:float=Field(...,gt=0,lt=1000000) # d
    
    
    
input_data = {
    "id": 1 ,#"1",
    "name": "John Doe",
    "is_active": False #"True"#"aa"
}

user= User(**input_data) # ** expansion operator
print(user)