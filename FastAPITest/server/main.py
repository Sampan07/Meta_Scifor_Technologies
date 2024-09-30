
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

# Get a student by ID
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Get all students
@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = crud.get_students(db=db, skip=skip, limit=limit)
    return students

# Update a student
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db=db, student_id=student_id, updated_student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Delete a student
@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
