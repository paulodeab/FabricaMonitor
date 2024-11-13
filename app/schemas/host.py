from pydantic import BaseModel

class HostCreate(BaseModel):

    id: int
    ip: str
    hostname: str
    mac_address: str
    operating_system: str

    class Config:
        orm_mode = True

class PortCreate(BaseModel):
    id: int
    port: int
    version: str
    service: str
    host_id: int
