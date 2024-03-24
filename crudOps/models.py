from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    student = "student"
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    middle_name: Optional[str] = None
    gender: Optional[Gender] = None
    role: Optional[List[Role]] = []