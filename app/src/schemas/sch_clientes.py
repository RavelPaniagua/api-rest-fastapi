from pydantic import BaseModel, Field, EmailStr

class Cliente(BaseModel):
    id: int = Field(minimum=1, description="ID del cliente")
    nombre: str = Field(min_length=1, max_length=100, description="Nombre del cliente")
    email: EmailStr
    telefono: str = Field(min_length=1, max_length=12, description="Teléfono del cliente")