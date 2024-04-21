
from fastapi import APIRouter, HTTPException
from typing import List
from Schemas.doctor import Doctor, DoctorCreate
from Services.doctor import DoctorService

router = APIRouter()
doctor_service = DoctorService()
doctor_service = DoctorService()

@router.get("/", response_model=List[Doctor])
def get_doctors():
    doctors = doctor_service.get_doctors()
    for doctor in doctors:
        doctor.message = "All Doctors found." 
    return doctors

@router.get("/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor.message = "Doctor found."
    return doctor

@router.post("/", response_model=Doctor, status_code=201)
def create_doctor(doctor_create: DoctorCreate):
    doctor = doctor_service.create_doctor(doctor_create)
    doctor.message = "Doctor created successfully."  # Set message to None initially
    return doctor


@router.put("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor_create: DoctorCreate):
    doctor = doctor_service.update_doctor(doctor_id, doctor_create)
    doctor.message = None  # Set message to None initially
    return doctor

@router.put("/{doctor_id}/availability", response_model=Doctor)
def set_doctor_availability(doctor_id: int, is_available: bool):
    try:
        doctor = doctor_service.set_doctor_availability(doctor_id, is_available)
        doctor.message = "Doctor availability status set successfully."  # Set message
        return doctor
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int):
    if not doctor_service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}
