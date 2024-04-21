from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int


patients_data = [
    Patient(id=1, name="John Doe", age=30, sex="Male", weight=75.5, height=1.75, phone="09070754352"),
    Patient(id=2, name="Jane Doe", age=25, sex="Female", weight=65.0, height=1.6, phone="09045763489"),
    Patient(id=3, name="Bob Smith", age=40, sex="Male", weight=80.0, height=1.85, phone="08078980954"),
]
