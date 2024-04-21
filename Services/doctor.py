
from typing import List
from Schemas.doctor import DoctorCreate, Doctor, doctor_data


class DoctorService:
    def __init__(self):
        self.doctors_db = doctor_data

    def get_available_doctors(self) -> List[Doctor]:
        return [doctor for doctor in self.doctors_db if doctor.is_available]

    def get_doctors(self) -> List[Doctor]:
        return self.doctors_db

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors_db:
            if doctor.id == doctor_id:
                return doctor
        raise ValueError("Doctor not found")

    def create_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        doctor_id = len(self.doctors_db) + 1
        doctor = Doctor(id=doctor_id, **doctor_data.dict())
        self.doctors_db.append(doctor)
        return doctor

    def update_doctor(self, doctor_id: int, doctor_data: DoctorCreate) -> Doctor:
        doctor = self.get_doctor_by_id(doctor_id)
        doctor.name = doctor_data.name
        doctor.specialization = doctor_data.specialization
        doctor.phone = doctor_data.phone
        return doctor

    def set_doctor_availability(self, doctor_id: int, is_available: bool) -> Doctor:
        for doctor in self.doctors_db:
            if doctor.id == doctor_id:
                doctor.is_available = is_available
                return doctor  # Return the updated Doctor object
        raise ValueError("Doctor not found")

    def delete_doctor(self, doctor_id: int):
        doctor = self.get_doctor_by_id(doctor_id)
        self.doctors_db.remove(doctor)

    


