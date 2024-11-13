from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Host(Base):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True, nullable=False)
    hostname = Column(String)
    mac_address = Column(String, nullable=False)
    operating_system = Column(String, nullable=False)

    # Corrigido: back_populates deve ser "host" para corresponder ao relacionamento em Port
    ports = relationship("Port", back_populates="host", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return (
            f"Host(id={self.id!r}, ip={self.ip!r}, "
            f"host_name={self.hostname!r}, mac_address={self.mac_address!r})"
        )

class Port(Base):
    __tablename__ = "port"

    id = Column(Integer, primary_key=True, index=True)
    port = Column(Integer, nullable=True)
    version = Column(String)
    service = Column(String, nullable=False)
    hosts_id = Column(Integer, ForeignKey('hosts.id'), nullable=False)

    # Relacionamento com a tabela Host
    host = relationship("Host", back_populates="ports")



