from datetime import datetime
from typing import List, Optional
from Schemas.appointment import AppointmentCreate, Appointment
from Services.doctor import DoctorService


class AppointmentService:
    def __init__(self, doctor_service):
        self.doctor_service = doctor_service
        self.appointments = []
        self.next_id = 1

    def create_appointment(self, appointment_create: AppointmentCreate) -> Appointment:
        available_doctors = self.doctor_service.get_available_doctors()
        selected_doctor = None
        
        # Find the doctor with the desired ID
        for doctor in available_doctors:
            if doctor.id == appointment_create.doctor_id:
                selected_doctor = doctor
                break
        
        if selected_doctor:
            appointment = Appointment(
                id=self.next_id,
                doctor_id=selected_doctor.id,
                patient_id=appointment_create.patient_id,
                datetime=appointment_create.datetime
            )
            self.next_id += 1  # Increment the next ID
            self.appointments.append(appointment)  # Add the appointment to the list
            return appointment
        else:
            raise ValueError("Selected doctor is not available")

    def complete_appointment(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                appointment.status = "Completed"
                appointment.completed_at = datetime.now()
                # Make the doctor available again
                self.doctor_service.set_doctor_availability(appointment.doctor_id, is_available=True)
                return appointment
        return None

    def cancel_appointment(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                appointment.status = "Cancelled"
                # Make the doctor available again
                self.doctor_service.set_doctor_availability(appointment.doctor_id, is_available=True)
                return appointment
        return None