import orm.modelos as modelos
from sqlalchemy.orm import Session

# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def compras_por_id(sesion:Session, id_usuario:int):
    print ("select * form app.compras where id = ", id_usuario)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id_usuario==id_usuario).first()

def fotos_por_id(sesion:Session, id_usuario:int):
    print ("select * form app.fotos where id = ", id_usuario)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_usuario==id_usuario).first()
