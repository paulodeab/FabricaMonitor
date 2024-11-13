
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Host(Base):

    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True, nullable=False)
    hostname = Column(String)
    mac_address = Column(String, nullable=False)
    operating_system = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Host(id={self.id!r}, ip={self.ip!r}, host_name={self.hostname!r}, mac_address={self.mac_address!r})"
        

