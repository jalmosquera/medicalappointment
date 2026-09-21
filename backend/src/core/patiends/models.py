from sqlmodel import SQLModel


class PatientCreate(SQLModel):
    name: str
    email: str
    age: int

