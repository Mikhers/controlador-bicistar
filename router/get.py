from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios, Venta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios, venta
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
from typing import List
import json

gets = APIRouter(
    prefix = "/ver"
)


@gets.get("",tags=["Documentación"])
def root():
    return {"message": "Hola, Soy la API de BiciStar"}

#=======================================================SEDE================================================================
#METODO GET
@gets.get("/sedes",tags=["Sedes"], response_model=List[Sede])
def allSede():
    with engine.connect() as conn:
        result = conn.execute(sede.select()).fetchall()
        return json.loads(json.dumps([dict(zip(('id_sede', 'nombre_sede', 'direccion_sede', 'ciudad_sede'), registro)) for registro in result])) 

#=======================================================proveedor================================================================
#METODO GET
@gets.get("/proveedores",tags=["Proveedores"], response_model=List[Proveedor])
def allProveedores():
    with engine.connect() as conn:
        result = conn.execute(proveedor.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_proveedor', 'nombre_proveedor', 'direccion_proveedor', 'telefono_proveedor','email_proveedor'), 
            registro)) for registro in result]))


#=======================================================PEDIDOS================================================================
#METODO GET
@gets.get("/pedidos",tags=["Pedidos"], response_model=List[Pedidos])
def allPedidos():
    with engine.connect() as conn:
        result = conn.execute(pedidos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'fecha_realizado', 'fecha_llegada', 'estado_pedido','total_pedido','id_sede','id_proveedor'),
            (registro[0], registro[1].isoformat(), registro[2].isoformat(), str(registro[3]), float(registro[4]), registro[5], registro[6])
            )) for registro in result]))
    
#=======================================================EMPLEADOS================================================================
#METODO GET
@gets.get("/empleados",tags=["Empleados"], response_model=List[Empleado])
def allEmpleados():
    with engine.connect() as conn:
        result = conn.execute(empleado.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_empleado', 'nombre_empleado', 'apellido_empleado', 'email_empleado','password_empleado','permiso_empleado','rol_empleado','salario_empleado','sede'),
            (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], float(registro[7]), registro[8])
            )) for registro in result]))

#=======================================================CATEGORIA-PRODUCTO================================================================
#METODO GET
@gets.get("/categoria-producto",tags=["Categoria-producto"], response_model=List[CategoriaProducto])
def allCategoriaProducto():
    with engine.connect() as conn:
        result = conn.execute(categoria_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_producto', 'nombre_categoria_producto', 'descripcion_categoria_producto'),
            registro)) for registro in result]))

#=======================================================Productos================================================================
#METODO GET
@gets.get("/productos",tags=["Productos"], response_model=List[Productos])
def allProductos():
    with engine.connect() as conn:
        result = conn.execute(productos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','cantidad_producto','stock','codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], registro[6], registro[7])
            )) for registro in result]))
    
#=======================================================PEDIDO-PRODUCTO================================================================
#METODO GET
@gets.get("/pedido-producto",tags=["Pedido-producto"], response_model=List[PedidoProducto])
def allPedidoProducto():
    with engine.connect() as conn:
        result = conn.execute(pedido_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido_producto','id_pedido', 'id_producto', 'cantidad_producto','precio_unitario'),
            (registro[0], registro[1], registro[2], registro[3], float(registro[4]))
            )) for registro in result]))
 
#=======================================================CategoriaServicio================================================================

#METODO GET
@gets.get("/categoria-servicio",tags=["Categoria-servicio"], response_model=List[CategoriaServicio])
def allCategoriaServicio():
    with engine.connect() as conn:
        result = conn.execute(categoria_servicio.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_servicio', 'nombre_servicio', 'descripcion_servicio'),
            registro)) for registro in result]))


#=======================================================CLIENTES================================================================
#METODO GET
@gets.get("/clientes",tags=["Clientes"], response_model=List[Clientes])
def allClientes():
    with engine.connect() as conn:
        result = conn.execute(clientes.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_cliente', 'nombre_cliente', 'apellido_cliente','telefono_cliente','email_cliente','cc_cliente','direccion_cliente'),
            registro)) for registro in result]))

#=======================================================SERVICIOS================================================================
#METODO GET
@gets.get("/servicios",tags=["Servicios"], response_model=List[Servicios])
def allServicios():
    with engine.connect() as conn:
        result = conn.execute(servicios.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_servicio', 'descripcion_servicio', 'fecha_servicio','precio_servicio','id_empleado','id_categoria_servicio','id_cliente'),
            (registro[0], registro[1], registro[2].isoformat(), float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))

#=======================================================Venta================================================================
#METODO GET
@gets.get("/ventas",tags=["Ventas"], response_model=List[Venta])
def allVentas():
    with engine.connect() as conn:
        result = conn.execute(venta.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_venta', 'fecha_venta', 'descripcion_venta','precio_venta','id_empleado','id_producto','id_cliente'),
            (registro[0], registro[1].isoformat(), registro[2], float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))


