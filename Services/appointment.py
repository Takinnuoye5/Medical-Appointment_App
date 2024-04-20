# app/entities/appointment/services.py

from typing import List, Optional
from datetime import datetime
from Schemas.appointment import Appointment, AppointmentCreate
from Services.doctor import DoctorService
from Services.patient import PatientService


class AppointmentService:
    def __init__(self):
        self.appointments = []
        self.last_id = 0

    def create_appointment(self, appointment_in: AppointmentCreate, doctor_service: DoctorService,
                           patient_service: PatientService) -> Appointment:
        self.last_id += 1
        appointment_data = appointment_in.dict()
        appointment_data["date"] = datetime.now()

        doctor_id = appointment_data.pop("doctor_id")
        patient_id = appointment_data.pop("patient_id")

        doctor = doctor_service.get_doctor(doctor_id)
        patient = patient_service.get_patient_by_id(patient_id)

        appointment = Appointment(id=self.last_id, doctor=doctor, patient=patient, **appointment_data)
        self.appointments.append(appointment)
        return appointment



    def get_appointment(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                return appointment
        return None

    def get_appointments(self) -> List[Appointment]:
        return self.appointments

    def delete_appointment(self, appointment_id: int) -> bool:
        for i, appointment in enumerate(self.appointments):
            if appointment.id == appointment_id:
                del self.appointments[i]
                return True
        return False
