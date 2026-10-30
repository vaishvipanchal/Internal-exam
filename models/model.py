from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2)
    course: str = Field(..., min_length=2)
    marks: float


class Student(StudentCreate):
    id: int