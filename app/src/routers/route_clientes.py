from fastapi import  APIRouter, Body, HTTPException, Response
from ..models.clientes import Clientes
from ..schemas.sch_clientes import Cliente

router_clientes = APIRouter()

@router_clientes.get("/clientes")
def get_clientes():
    try:
        clientes = Clientes()
        return clientes.get_clientes()
    except Exception as e:
        return {"error": str(e)}

@router_clientes.post("/clientes")
def create_clientes(client:Cliente = Body()):
    clientes = Clientes()
    if clientes.create_cliente(client.nombre, client.email, client.telefono):
        return Response(status_code=201, content="Cliente creado correctamente")
    else:
        raise HTTPException(status_code=400, detail="Error al crear el cliente")

@router_clientes.put("/clientes/{cliente_id}")
def update_clientes(cliente_id: int ,  cliente: Cliente = Body()):
    if cliente_id != cliente.id:
        return Response(status_code=400, content="El ID del cliente no coincide con el ID proporcionado en el cuerpo de la solicitud")
    clientes = Clientes()
    if clientes.update_cliente(cliente_id, cliente.nombre, cliente.email, cliente.telefono):
        return Response(status_code=200, content="Cliente actualizado correctamente")
    else:
        raise Response(status_code=400, content="Error al actualizar el cliente")

@router_clientes.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int):
    clientes = Clientes()
    if clientes.delete_cliente(cliente_id):
        return Response(status_code=200, content="Cliente eliminado correctamente")
    else: 
        raise Response(status_code=400, content="Error al eliminar el cliente")

     