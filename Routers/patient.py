
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from Schemas.patient import Patient, PatientCreate
from Services.patient import PatientService

router = APIRouter()
patient_service = PatientService()


@router.get("/", response_model=List[Patient])
def get_patients():
    return patient_service.get_patients()


@router.get("/{patient_id}", response_model=Patient)
async def get_patient(patient_id: int):
    patient = patient_service.get_patient_by_id(patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient id not found")
    return patient


@router.post("/", response_model=Patient, status_code=201)
def create_patient(patient_create: PatientCreate):
    return patient_service.create_patient(patient_create)


@router.put("/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient_update: PatientCreate):
    patient = patient_service.update_patient(patient_id, patient_update)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.delete("/{patient_id}")
async def delete_patient(patient_id: int):
    if not patient_service.delete_patient(patient_id):
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}
