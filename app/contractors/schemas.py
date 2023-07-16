from pydantic import BaseModel, EmailStr


class ContractorsSchemas(BaseModel):
    id: int
    name: str
    inn: int
    kpp: int
    address_juridical: str
    address_actual: str
    phone: str
    email: EmailStr
    hide: bool

    class Config:
        orm_mode = True
