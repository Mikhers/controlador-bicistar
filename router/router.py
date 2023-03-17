from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios, Venta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios, venta
from config.db import engine
from typing import List

from datetime import datetime
import json

bicistar = APIRouter()


@bicistar.get("/",tags=["Documentación"])
def root():
    return {"message": "Hola, Soy la API de BiciStar"}



#GET########################################################################################################################

#=======================================================SEDE================================================================
@bicistar.get("/ver-sedes",tags=["Sedes"], response_model=List[Sede])
def allSede():
    with engine.connect() as conn:
        result = conn.execute(sede.select()).fetchall()
        return json.loads(json.dumps([dict(zip(('id_sede', 'nombre_sede', 'direccion_sede', 'ciudad_sede'), registro)) for registro in result])) 

#=======================================================proveedor================================================================
@bicistar.get("/ver-proveedores",tags=["Provedores"], response_model=List[Proveedor])
def allProveedores():
    with engine.connect() as conn:
        result = conn.execute(proveedor.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_proveedor', 'nombre_proveedor', 'direccion_proveedor', 'telefono_proveedor','email_proveedor'), 
            registro)) for registro in result]))

#=======================================================PEDIDOS================================================================
@bicistar.get("/ver-pedidos",tags=["Pedidos"], response_model=List[Pedidos])
def allPedidos():
    with engine.connect() as conn:
        result = conn.execute(pedidos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'fecha_realizado', 'fecha_llegada', 'estado_pedido','total_pedido','id_sede','id_proveedor'),
            (registro[0], registro[1].isoformat(), registro[2].isoformat(), str(registro[3]), float(registro[4]), registro[5], registro[6])
            )) for registro in result]))
#=======================================================EMPLEADOS================================================================
@bicistar.get("/ver-empleados",tags=["Empleados"], response_model=List[Empleado])
def allEmpleados():
    with engine.connect() as conn:
        result = conn.execute(empleado.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_empleado', 'nombre_empleado', 'apellido_empleado', 'email_empleado','password_empleado','permiso_empleado','rol_empleado','salario_empleado','sede'),
            (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], float(registro[7]), registro[8])
            )) for registro in result]))
#=======================================================CATEGORIA-PRODUCTO================================================================
@bicistar.get("/ver-categoria-producto",tags=["categoria_producto"], response_model=List[CategoriaProducto])
def allCategoriaProducto():
    with engine.connect() as conn:
        result = conn.execute(categoria_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_producto', 'nombre_categoria_producto', 'descripcion_categoria_producto'),
            registro)) for registro in result]))
#=======================================================SEDE================================================================
@bicistar.get("/ver-productos",tags=["Productos"], response_model=List[Productos])
def allProductos():
    with engine.connect() as conn:
        result = conn.execute(productos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','cantidad_producto','stock','codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], registro[6], registro[7])
            )) for registro in result]))
#=======================================================PEDIDO-PRODUCTO================================================================
@bicistar.get("/ver-pedido-producto",tags=["pedido-producto"], response_model=List[PedidoProducto])
def allPedidoProducto():
    with engine.connect() as conn:
        result = conn.execute(pedido_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'id_producto', 'cantidad_producto','precio_unitario'),
            (registro[0], registro[1], registro[2], float(registro[3]))
            )) for registro in result]))
#=======================================================CategoriaServicio================================================================
@bicistar.get("/ver-categoria-servicio",tags=["categoria-servicio"], response_model=List[CategoriaServicio])
def allCategoriaServicio():
    with engine.connect() as conn:
        result = conn.execute(categoria_servicio.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_servicio', 'nombre_servicio', 'descripcion_servicio'),
            registro)) for registro in result]))
#=======================================================CategoriaServicio================================================================
@bicistar.get("/ver-clientes",tags=["Clientes"], response_model=List[Clientes])
def allClientes():
    with engine.connect() as conn:
        result = conn.execute(clientes.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_cliente', 'nombre_cliente', 'apellido_cliente','telefono_cliente','email_cliente','cc_cliente','direccion_cliente'),
            registro)) for registro in result]))
#=======================================================SERVICIOS================================================================
@bicistar.get("/ver-servicios",tags=["Servicios"], response_model=List[Servicios])
def allServicios():
    with engine.connect() as conn:
        result = conn.execute(servicios.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_servicio', 'descripcion_servicio', 'fecha_servicio','precio_servicio','id_empleado','id_categoria_servicio','id_cliente'),
            (registro[0], registro[1], registro[2].isoformat(), float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))
#=======================================================SERVICIOS================================================================
@bicistar.get("/ver-ventas",tags=["Ventas"], response_model=List[Venta])
def allVentas():
    with engine.connect() as conn:
        result = conn.execute(venta.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_venta', 'fecha_venta', 'descripcion_venta','precio_venta','id_empleado','id_producto','id_cliente'),
            (registro[0], registro[1].isoformat(), registro[2], float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))

#POST################################################################################################################################
#####################################################################################################################################

@bicistar.post("/insert-sede", status_code=HTTP_201_CREATED)
def insertSede(data: Sede):
    with engine.connect() as conn:
        conn.execute(sede.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

