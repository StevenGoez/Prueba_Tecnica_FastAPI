from uuid import UUID
from pydantic import BaseModel

class AddressCreate(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
    email: str

class Address(BaseModel):
    address_id: UUID
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
