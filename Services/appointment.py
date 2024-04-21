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
            # Create the appointment
            appointment = Appointment(
                id=self.next_id,
                doctor_id=selected_doctor.id,
                patient_id=appointment_create.patient_id,
                datetime=appointment_create.datetime,
                message="Appointment created successfully."
            )
            self.next_id += 1
            self.appointments.append(appointment)
            
            # Set the doctor as booked for the appointment time
            self.doctor_service.set_doctor_availability(selected_doctor.id, is_available=False)
            
            return appointment
        else:
            raise ValueError("Selected doctor is not available")

    def complete_appointment(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                appointment.status = "Completed"
                appointment.completed_at = datetime.now()
                appointment.message = "Appointment completed successfully."
                # Make the doctor available again
                self.doctor_service.set_doctor_availability(appointment.doctor_id, is_available=True)
                return appointment
        return None

    def cancel_appointment(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                appointment.status = "Cancelled"
                appointment.message = "Appointment cancelled."
                # Make the doctor available again
                self.doctor_service.set_doctor_availability(appointment.doctor_id, is_available=True)
                return appointment
        return None

    def get_all_appointments(self) -> List[Appointment]:
        return self.appointments

    def get_completed_appointments(self) -> List[Appointment]:
        return [appointment for appointment in self.appointments if appointment.status == "Completed"]

    def get_cancelled_appointments(self) -> List[Appointment]:
        return [appointment for appointment in self.appointments if appointment.status == "Cancelled"]
