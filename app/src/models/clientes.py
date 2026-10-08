from ...config import conexion
from sqlalchemy import text

class Clientes:
    def __init__(self):
        self.conexion = conexion.conexion
        self.table_name = "clientes"

    def get_clientes(self):
        with conexion.conexion.connect() as conn:
            result = conn.execute(text("SELECT * FROM clientes"))
            clients = []
            for row in result:
                clients.append({"id":row[0],"nombre":row[1]})
            return clients

    def create_cliente(self, nombre, email, telefono):
        with conexion.conexion.connect() as conn:
            result = conn.execute(text("INSERT INTO clientes (nombre,email,telefono) VALUES (:nombre,:email,:telefono)"),
                          {"nombre": nombre, "email": email, "telefono": telefono},)
            conn.commit()
            return result
     

    def update_cliente(self,id,nombre, email, telefono):
        with conexion.conexion.connect() as conn:
            result = conn.execute(text("UPDATE clientes SET nombre = :nombre, email= :email, telefono= :telefono WHERE id_cliente = :id"),
                         {"nombre": nombre, "id": id, "email": email, "telefono": telefono},)
            conn.commit()
            return result

    def delete_cliente(self,id):
        with conexion.conexion.connect() as conn:
           result = conn.execute(text("DELETE FROM clientes WHERE id_cliente = :id"),
                         {"id": id},)
           conn.commit()
           print(result)
           return result
