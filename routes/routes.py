from fastapi import APIRouter, status
from typing import List

from models.model import Student, StudentCreate
from controllers.controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter()


# create
@router.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student_api(student: StudentCreate):
    return create_student(student)


# get
@router.get(
    "/students",
    response_model=List[Student],
    status_code=status.HTTP_200_OK
)
def get_all_students_api():
    return get_all_students()


# get by id
@router.get(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student_api(student_id: int):
    return get_student_by_id(student_id)


# update
@router.put(
    "/students/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update_student_api(
    student_id: int,
    student: StudentCreate
):
    return update_student(student_id, student)


# delete
@router.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student_api(student_id: int):
    delete_student(student_id)