from fastapi import HTTPException
from models.model import Student, StudentCreate


# In-memory storage
students = []

# ID counter
next_id = 1


def create_student(student_data: StudentCreate):
    global next_id

    student = Student(
        id=next_id,
        name=student_data.name,
        course=student_data.course,
        marks=student_data.marks
    )

    students.append(student)
    next_id += 1

    return student


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def update_student(student_id: int, student_data: StudentCreate):
    for index, student in enumerate(students):

        if student.id == student_id:

            updated_student = Student(
                id=student_id,
                name=student_data.name,
                course=student_data.course,
                marks=student_data.marks
            )

            students[index] = updated_student

            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def delete_student(student_id: int):
    for index, student in enumerate(students):

        if student.id == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )