from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from datetime import datetime
# from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios, Venta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios
# from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
# from typing import List
# import json

deletes = APIRouter(
    prefix = "/delete"
)


#METODO DELETE
@deletes.delete("/sede/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Sedes'])
def dropSede(id: int):
    with engine.connect() as conn:
        conn.execute(sede.update().values(deleted_at=datetime.now()).where(sede.c.id_sede == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)


#======================================================================================================================================================================
@deletes.delete("/proveedor/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Proveedores'])
def dropProveedor(id: int):
    with engine.connect() as conn:
        conn.execute(proveedor.update().values(deleted_at=datetime.now()).where(proveedor.c.id_proveedor == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)


#======================================================================================================================================================================
# @deletes.delete("/pedido/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Pedidos'])
# def dropPedido(id: int):
#     with engine.connect() as conn:
#         conn.execute(pedidos.delete().where(pedidos.c.id_pedido == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)
    
#======================================================================================================================================================================
# @deletes.delete("/empleado/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Empleados'])
# def dropEmpleados(id: int):
#     with engine.connect() as conn:
#         conn.execute(empleado.delete().where(empleado.c.id_empleado == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)

#======================================================================================================================================================================
# @deletes.delete("/categoria-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-producto'])
# def dropCategoriaProducto(id: int):
#     with engine.connect() as conn:
#         conn.execute(categoria_producto.delete().where(categoria_producto.c.id_categoria_producto == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)
    
#======================================================================================================================================================================
# @deletes.delete("/producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Productos'])
# def dropProducto(id: int):
#     with engine.connect() as conn:
#         conn.execute(productos.delete().where(productos.c.id_producto == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)

#======================================================================================================================================================================
# @deletes.delete("/pedido-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Pedido-producto'])
# def dropPedidoProducto(id: int):
#     with engine.connect() as conn:
#         conn.execute(pedido_producto.delete().where(pedido_producto.c.id_pedido_producto == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)

#======================================================================================================================================================================
# @deletes.delete("/categoria-servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-servicio'])
# def dropCategoriaServicio(id: int):
#     with engine.connect() as conn:
#         conn.execute(categoria_servicio.delete().where(categoria_servicio.c.id_categoria_servicio == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)

#======================================================================================================================================================================
# @deletes.delete("/cliente/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Clientes'])
# def dropClientes(id: int):
#     with engine.connect() as conn:
#         conn.execute(clientes.delete().where(clientes.c.id_cliente == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)
    
#======================================================================================================================================================================
# @deletes.delete("/servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Servicios'])
# def dropServicios(id: int):
#     with engine.connect() as conn:
#         conn.execute(servicios.delete().where(servicios.c.id_servicio == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)
    
#======================================================================================================================================================================
# @deletes.delete("/ventas/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Ventas'])
# def dropVenta(id: int):
#     with engine.connect() as conn:
#         conn.execute(venta.delete().where(venta.c.id_venta == id))
#         conn.commit()
#         return Response(status_code=HTTP_204_NO_CONTENT)