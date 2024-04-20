# app/entities/patient/services.py

from typing import List, Optional
from Schemas.patient import Patient, PatientCreate


class PatientService:
    def __init__(self):
        self.patients = []
        self.id_counter = 1

    def create_patient(self, patient_create: PatientCreate) -> Patient:
        patient = Patient(id=self.id_counter, **patient_create.dict())
        self.patients.append(patient)
        self.id_counter += 1
        return patient

    def get_patients(self) -> List[Patient]:
        return self.patients

    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def update_patient(self, patient_id: int, patient_create: PatientCreate) -> Optional[Patient]:
        for patient in self.patients:
            if patient.id == patient_id:
                patient.name = patient_create.name
                patient.age = patient_create.age
                patient.sex = patient_create.sex
                patient.weight = patient_create.weight
                patient.height = patient_create.height
                patient.phone = patient_create.phone
                return patient
        return None

    def delete_patient(self, patient_id: int) -> bool:
        for i, patient in enumerate(self.patients):
            if patient.id == patient_id:
                del self.patients[i]
                return True
        return False
