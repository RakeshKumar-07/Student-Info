from fastapi import APIRouter, Body, Request, HTTPException, status
from typing import List

from models import Student, StudentUpdate

router = APIRouter()

@router.get("/", response_description="List all students", response_model=List[Student])
def list_students(request: Request):
    students = list(request.app.database["students"].find({}))
    return students

@router.post("/", response_description="Create a new student", status_code=status.HTTP_201_CREATED, response_model=Student)
def create_student(request: Request, student: Student = Body(...)):
    student_dict = student.dict()
    inserted_student = request.app.database["students"].insert_one(student_dict)
    created_student = request.app.database["students"].find_one({"_id": inserted_student.inserted_id})
    return created_student

@router.get("/{id}", response_description="Get a single student by id", response_model=Student)
def find_student(id: str, request: Request):
    student = request.app.database["students"].find_one({"id": id})
    if student:
        return student
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

@router.put("/{id}", response_description="Update a student", response_model=Student)
def update_student(id: str, request: Request, student: StudentUpdate = Body(...)):
    student_dict = student.dict(exclude_unset=True)  # Exclude unset fields
    updated_student = request.app.database["students"].find_one_and_update(
        {"id": id}, {"$set": student_dict}, return_document=True
    )
    if updated_student:
        return updated_student
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

@router.delete("/{id}", response_description="Delete a student")
def delete_student(id: str, request: Request):
    deleted_student = request.app.database["students"].find_one_and_delete({"id": id})
    if deleted_student:
        return {"message": f"Student with ID {id} deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")