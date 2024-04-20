from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int
    is_available: bool = True
