from sqlalchemy.orm import Session
from app.schemas.host import HostCreate
from app.models import host_model

def create_host(db: Session, host: HostCreate):
    db_host = host_model.Host(
        id=host.id,
        ip=host.ip,
        hostname=host.hostname,
        mac_address=host.mac_address,
        operating_system= host.operating_system
    )
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return db_host

