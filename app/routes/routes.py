from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import host
from app.services.scan_net import ScanNetwork
from crud.database import SessionLocal
from crud import host_crud

router = APIRouter()

# # Função geradora para obter a sessão do banco de dados
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.get("/scan")
def get_data():
    try:
        scan = ScanNetwork()
        scan.set_ip()
        scan.scan_network()
        return scan.generate_json()
    except Exception as e:
        return {"Error": str(e)}
    

# @router.post("/save_hosts")
# def create_host(host: host.HostCreate,  db: Session = Depends(get_db)):
#     try:
#         # Use a sessão 'db' injetada corretamente
#         result_host = host_crud.create_host(db, host)
#         print(result_host)
#         # return host_crud.create_host(db, host)
#     except Exception as e:
#         raise HTTPException(status_code=501, detail=f"Erro ao salvar: {e}")
    

