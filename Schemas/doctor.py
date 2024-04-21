from pydantic import BaseModel
from typing import Optional


class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorCreate(DoctorBase):
    is_available: bool = True
    is_booked: bool = False  

class Doctor(DoctorBase):
    id: int
    is_available: bool
    is_booked: bool
    message: Optional[str]  # Optional message field

doctor_data = [
    Doctor(id=1, name="Dr Femi", specialization="Cardiology", phone="09070754352", is_available=True, is_booked=False, message=None),
    Doctor(id=2, name="Dr Tunde", specialization="Dermatology", phone="09045763489", is_available=True, is_booked=False, message=None),
    Doctor(id=3, name="Dr Simeon", specialization="Neurology", phone="08078980954", is_available=True, is_booked=False, message=None),
]
