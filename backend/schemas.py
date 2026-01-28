from pydantic import BaseModel, ConfigDict
from fastapi_users import schemas
from datetime import datetime
import uuid


class PostCreate(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    caption: str | None
    url: str
    file_type: str
    file_name: str
    created_at: datetime
    email: str 
    is_owner: bool

    model_config = ConfigDict(from_attributes=True)


class PostResponse(BaseModel):
    title: str
    content: str

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

