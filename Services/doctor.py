from typing import List, Optional
from Schemas.doctor import Doctor, DoctorCreate


class DoctorService:
    def __init__(self):
        self.doctors = []
        self.last_id = 0

    def create_doctor(self, doctor_in: DoctorCreate) -> Doctor:
        self.last_id += 1
        doctor = Doctor(id=self.last_id, **doctor_in.dict())
        self.doctors.append(doctor)
        return doctor

    def get_doctor(self, doctor_id: int) -> Optional[Doctor]:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def get_doctors(self) -> List[Doctor]:
        return self.doctors

    def update_doctor(self, doctor_id: int, doctor_in: DoctorCreate) -> Optional[Doctor]:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                doctor.name = doctor_in.name
                doctor.specialization = doctor_in.specialization
                doctor.phone = doctor_in.phone
                return doctor
        return None

    def delete_doctor(self, doctor_id: int) -> bool:
        for i, doctor in enumerate(self.doctors):
            if doctor.id == doctor_id:
                del self.doctors[i]
                return True
        return False
