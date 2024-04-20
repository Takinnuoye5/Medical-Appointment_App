
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from Schemas.appointment import Appointment, AppointmentCreate
from Services.appointment import AppointmentService
from Services.doctor import DoctorService
from Services.patient import PatientService

router = APIRouter()
appointment_service = AppointmentService()
doctor_service = DoctorService()
patient_service = PatientService()

@router.post("/", response_model=Appointment, status_code=201)
def create_appointment(appointment_in: AppointmentCreate):
    patient = patient_service.get_patients(appointment_in.patient_id)
    appointment = appointment_service.create_appointment(appointment_in, doctor_service, patient_service, patient)
    return appointment

@router.get("/", response_model=List[Appointment])
def read_appointments():
    return appointment_service.get_appointments()

@router.get("/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int):
    appointment = appointment_service.get_appointment(appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int):
    if not appointment_service.delete_appointment(appointment_id):
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}
