import os

from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Deploy Cloud", version="1.0.0")

class PostInput(BaseModel):
    nombre: str = Field(min_length=1, example="Juan")
    edad: int = Field(ge=0, example=30)
    numero: float = Field(gt=0, example=3.14)

class PostOutput(BaseModel):
    frase: str
    calculo: float

@app.get("/")
def getName() -> dict[str, str]:
    nombre = os.getenv("FIRST_NAME", "Nombre")
    apellido = os.getenv("LAST_NAME", "Apellido")
    return {"nombre": nombre, "apellido": apellido}

@app.get("/{number}")
def calculate(number: int) -> dict[str, int]:
    return {"Resultado del cálculo": (number + 5) * 2}

@app.post("/", response_model = PostOutput)
def build_phrase(payload: PostInput) -> PostOutput:
    division = payload.edad / payload.numero
    frase = f"Hola {payload.nombre}, tu edad es {payload.edad}, si la divides por {payload.numero} el resultado es {division}"
    return PostOutput(frase = frase, calculo = division)