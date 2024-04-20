from fastapi import FastAPI
from Routers import appointment, doctor, patient
from fastapi import HTTPException
from fastapi.responses import Response


app = FastAPI()


@app.get("/", status_code=200)
def home():
    return {"message": "hello welcome to the hospital"}



app.include_router(patient.router, prefix="/patient", tags=["patient"])
app.include_router(doctor.router, prefix="/doctor", tags=["doctor"])
app.include_router(appointment.router, prefix="/appointment", tags=["appointment"])