from fastapi import APIRouter, HTTPException, Depends
from Services.appointment import AppointmentService
from Services.doctor import DoctorService
from Schemas.appointment import AppointmentCreate, Appointment

router = APIRouter()
doctor_service = DoctorService()  # Instantiate DoctorService
appointment_service = AppointmentService(doctor_service)  # Instantiate AppointmentService

@router.post("/", response_model=Appointment, status_code=201)
def create_appointment(
    appointment_create: AppointmentCreate,
):
    try:
        appointment = appointment_service.create_appointment(appointment_create)
        return appointment
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.put("/{appointment_id}/complete", response_model=Appointment)
def complete_appointment(
    appointment_id: int,
):
    appointment = appointment_service.complete_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.put("/{appointment_id}/cancel", response_model=Appointment)
def cancel_appointment(
    appointment_id: int,
):
    appointment = appointment_service.cancel_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
