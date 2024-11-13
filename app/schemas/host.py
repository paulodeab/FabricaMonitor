from typing import List
from pydantic import BaseModel


class PortCreate(BaseModel):
    id: int
    port: int
    version: str
    service: str
    host_id: int


class HostCreate(BaseModel):

    id: int
    ip: str
    hostname: str
    mac_address: str
    operating_system: str
    ports: List[PortCreate]

    class Config:
        orm_mode = True