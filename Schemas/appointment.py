from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: Optional[int] = None
    status: str = "Pending"
    completed_at: Optional[datetime] = None
    datetime: datetime


class AppointmentCreate(AppointmentBase):
    datetime: datetime


class Appointment(AppointmentBase):
    id: Optional[int] = None
