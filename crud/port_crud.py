from sqlalchemy.orm import Session
from app.models import host_model
from app.schemas.host import PortCreate


def creat_port(db: Session, port: PortCreate):
    db_port = host_model.Port(
        id       = port.id,
        port     = port.port,
        version  = port.version,
        service  = port.service,
        hosts_id = port.host_id
    )
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port
