# app/entities/doctor/routers.py

from fastapi import APIRouter, HTTPException
from typing import List, Optional
from Schemas.doctor import Doctor, DoctorCreate
from Services.doctor import DoctorService

router = APIRouter()
doctor_service = DoctorService()


@router.post("/", response_model=Doctor, status_code=201)
def create_doctor(doctor_in: DoctorCreate):
    return doctor_service.create_doctor(doctor_in)


@router.get("/", response_model=List[Doctor])
def read_doctors():
    return doctor_service.get_doctors()


@router.get("/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int):
    doctor = doctor_service.get_doctor(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@router.put("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor_in: DoctorCreate):
    doctor = doctor_service.update_doctor(doctor_id, doctor_in)
    if doctor is None:
        raise HTTPException(status_code=404, detail="No Doctor with the ID")
    return doctor


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int):
    if not doctor_service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor does not exist")
    return {"message": "Doctor deleted successfully"}
