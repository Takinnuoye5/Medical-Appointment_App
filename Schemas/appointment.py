from pydantic import BaseModel, validator
from datetime import datetime
from Schemas.patient import Patient
from Schemas.doctor import Doctor


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime

    @validator("patient_id")
    def patient_id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("must be a positive integer")
        return v

    @validator("doctor_id")
    def doctor_id_must_be_positive(cls, d):
        if d <= 0:
            raise ValueError("must be a positive integer")
        return d


class AppointmentCreate(AppointmentBase):
    patient: Patient
    doctor: Doctor


class Appointment(AppointmentBase):
    id: int
    
