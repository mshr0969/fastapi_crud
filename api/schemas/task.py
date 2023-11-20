from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="study")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="done flag")

    class Config:
        orm_mode = True


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
