from sqlalchemy import and_
from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_406_NOT_ACCEPTABLE
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios,SedesProductos, Factura, ServicioVenta,ProductoVenta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios,sedes_productos, factura,servicio_venta,producto_venta
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

@gets.get("/sedes",tags=["Sedes"], response_model=List[Sede])
def allSede():
    with engine.connect() as conn:
        result = conn.execute(sede.select().where(sede.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(('id_sede', 'nombre_sede', 'direccion_sede', 'ciudad_sede'), registro)) for registro in result])) 

@gets.get("/sedes/{id}",tags=["Sedes"], response_model=Sede)
def allSede(id: int):
    with engine.connect() as conn:
        result = conn.execute(sede.select().where(and_(sede.c.deleted_at == None, sede.c.id_sede == id))).first()
        return {'id_sede':result[0],'nombre_sede':result[1],'direccion_sede':result[2],'ciudad_sede':result[3]}

#=======================================================proveedor================================================================
# METODO GET
@gets.get("/proveedores",tags=["Proveedores"], response_model=List[Proveedor])
def allProveedores():
    with engine.connect() as conn:
        result = conn.execute(proveedor.select().where(proveedor.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_proveedor', 'nombre_proveedor', 'direccion_proveedor', 'telefono_proveedor','email_proveedor'), 
            registro)) for registro in result]))

#=======================================================EMPLEADOS================================================================

@gets.get("/empleados",tags=["Empleados"], response_model=List[Empleado])
def allEmpleados():
    with engine.connect() as conn:
        result = conn.execute(empleado.select().where(empleado.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_empleado', 'nombre_empleado', 'apellido_empleado', 'email_empleado','password_empleado','permiso_empleado','rol_empleado','salario_empleado','id_sede'),
            (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], float(registro[7]), registro[8])
            )) for registro in result]))

@gets.get("/empleados/{id}",tags=["Empleados"], response_model=Empleado)
def allEmpleados(id:int):
    with engine.connect() as conn:
        result = conn.execute(empleado.select().where(and_(empleado.c.deleted_at == None,empleado.c.id_empleado == id))).first()
        return {'id_empleado':result[0], "nombre_empleado":result[1], "apellido_empleado":result[2], "email_empleado":result[3], "password_empleado":result[4],
                 "permiso_empleado":result[5], "rol_empleado":result[6], "salario_empleado":float(result[7]), "id_sede":result[8]}

#=======================================================PEDIDOS================================================================

@gets.get("/pedidos",tags=["Pedidos"], response_model=List[Pedidos])
def allPedidos():
    with engine.connect() as conn:
        result = conn.execute(pedidos.select().where(pedidos.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'fecha_realizado', 'fecha_llegada', 'estado_pedido','total_pedido','id_sede','id_proveedor','id_empleado'),
            (registro[0], registro[1].isoformat(), registro[2].isoformat(), str(registro[3]), float(registro[4]), registro[5], registro[6], registro[7])
            )) for registro in result]))

@gets.get("/pedidos/{id}",tags=["Pedidos"], response_model=Pedidos)
def allPedidos(id:int):
    with engine.connect() as conn:
        result = conn.execute(pedidos.select().where(and_(pedidos.c.deleted_at == None,pedidos.c.id_pedido == id))).first()
        return {'id_pedido':result[0], 'fecha_realizado':result[1].isoformat(), 'fecha_llegada':result[2].isoformat(), 
                'estado_pedido':str(result[3]), 'total_pedido':float(result[4]), 'id_sede':result[5], 'id_proveedor':result[6], 'id_empleado':result[7]}
    

#=======================================================CATEGORIA-PRODUCTO================================================================

@gets.get("/categoria-producto",tags=["Categoria-producto"], response_model=List[CategoriaProducto])
def allCategoriaProducto():
    with engine.connect() as conn:
        result = conn.execute(categoria_producto.select().where(categoria_producto.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_producto', 'nombre_categoria_producto', 'descripcion_categoria_producto'),
            registro)) for registro in result]))
    
@gets.get("/categoria-producto/{id}",tags=["Categoria-producto"], response_model=CategoriaProducto)
def getIdCategoriaProducto(id: int):
    with engine.connect() as conn:
        result = conn.execute(categoria_producto.select().where(and_(categoria_producto.c.deleted_at == None, categoria_producto.c.id_categoria_producto == id))).first()
        if(result):
            return {"id_categoria_producto":result[0], "nombre_categoria_producto":result[1], "descripcion_categoria_producto":result[2]}
        return Response(status_code=HTTP_406_NOT_ACCEPTABLE)

#=======================================================Productos================================================================

@gets.get("/productos",tags=["Productos"], response_model=List[Productos])
def allProductos():
    with engine.connect() as conn:
        result = conn.execute(productos.select().where(productos.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto', 'codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5])
            )) for registro in result]))
    
@gets.get("/productos/{id}",tags=["Productos"], response_model=Productos)
def getIdProducto(id: int):
    with engine.connect() as conn:
        result = conn.execute(productos.select().where(productos.c.id_producto == id)).first()
        if(result):
            return {"id_producto":result[0], "nombre_producto":result[1], "descripcion_producto":result[2], "precio_producto":result[3],"codigo_producto":result[4],"id_categoria_producto": result[5]}
        return Response(status_code=HTTP_406_NOT_ACCEPTABLE)
#=======================================================sedes-productos================================================================
@gets.get("/sedes-productos",tags=["Sedes-Productos"], response_model=List[SedesProductos])
def allSedesProductos():
    with engine.connect() as conn:
        result = conn.execute(sedes_productos.select().where(sedes_productos.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_sede', 'id_producto', 'stock'),
            (registro[0], registro[1], registro[2])
            )) for registro in result]))

@gets.get("/sedes-productos/{id}",tags=["Sedes-Productos"], response_model=List[SedesProductos])
def sedeSedesProductos(id:int):
    with engine.connect() as conn:
        result = conn.execute(sedes_productos.select().where(and_(sedes_productos.c.deleted_at == None, sedes_productos.c.id_sede == id))).fetchall()
        if(result):return json.loads(json.dumps([dict(zip(
            ('id_sede', 'id_producto', 'stock'),
            (registro[0], registro[1], registro[2])
            )) for registro in result]))
        return Response(status_code=HTTP_406_NOT_ACCEPTABLE)
    
@gets.get("/sedes-productos/{id}/{idd}",tags=["Sedes-Productos"], response_model=SedesProductos)
def verSedesProductos(id:int, idd:int):
    with engine.connect() as conn:
        result = conn.execute(sedes_productos.select().where(and_(sedes_productos.c.deleted_at == None, sedes_productos.c.id_sede == id, sedes_productos.c.id_producto == idd))).first()
        if(result):return {'id_sede':result[0], 'id_producto':result[1], 'stock':result[2]}
        return Response(status_code=HTTP_406_NOT_ACCEPTABLE)
#=======================================================PEDIDO-PRODUCTO================================================================

@gets.get("/pedido-producto",tags=["Pedido-producto"], response_model=List[PedidoProducto])
def allPedidoProducto():
    with engine.connect() as conn:
        result = conn.execute(pedido_producto.select().where(pedido_producto.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'id_producto', 'cantidad_producto','precio_unitario'),
            (registro[0], registro[1], registro[2], float(registro[3]))
            )) for registro in result]))
 
@gets.get("/pedido-producto/{id}",tags=["Pedido-producto"], response_model=List[PedidoProducto])
def pedidoPedidoProducto(id:int):
    with engine.connect() as conn:
        result = conn.execute(pedido_producto.select().where(and_(pedido_producto.c.deleted_at == None, pedido_producto.c.id_pedido == id))).fetchall()
        if(result):return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'id_producto', 'cantidad_producto','precio_unitario'),
            (registro[0], registro[1], registro[2],  float(registro[3]))
            )) for registro in result]))
        return Response(status_code=HTTP_406_NOT_ACCEPTABLE)
        
#=======================================================CategoriaServicio================================================================


@gets.get("/categoria-servicio",tags=["Categoria-servicio"], response_model=List[CategoriaServicio])
def allCategoriaServicio():
    with engine.connect() as conn:
        result = conn.execute(categoria_servicio.select().where(categoria_servicio.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_servicio', 'nombre_servicio', 'descripcion_servicio'),
            registro)) for registro in result]))

#=======================================================SERVICIOS================================================================

@gets.get("/servicios",tags=["Servicios"], response_model=List[Servicios])
def allServicios():
    with engine.connect() as conn:
        result = conn.execute(servicios.select().where(servicios.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_servicio', 'nombre_servicio', 'descripcion_servicio','precio_servicio','id_categoria_servicio'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4])
            )) for registro in result]))

#=======================================================CLIENTES================================================================

@gets.get("/clientes",tags=["Clientes"], response_model=List[Clientes])
def allClientes():
    with engine.connect() as conn:
        result = conn.execute(clientes.select().where(clientes.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_cliente', 'nombre_cliente', 'apellido_cliente','telefono_cliente','email_cliente','cc_cliente','direccion_cliente'),
            registro)) for registro in result]))


#=======================================================factura================================================================

@gets.get("/facturas",tags=["Facturas"], response_model=List[Factura])
def allFactura():
    with engine.connect() as conn:
        result = conn.execute(factura.select().where(factura.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'fecha_factura', 'total','codigo_factura','id_empleado','id_cliente','id_sede'),
            (registro[0], registro[1].isoformat(), float(registro[2]), registro[3],  registro[4], registro[5], registro[6])
            )) for registro in result]))

@gets.get("/facturas/{id}",tags=["Facturas"], response_model=List[Factura])
def verFactura(id:int):
    with engine.connect() as conn:
        result = conn.execute(factura.select().where(and_(factura.c.deleted_at == None, factura.c.id_factura == id))).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'fecha_factura', 'total','codigo_factura','id_empleado','id_cliente','id_sede'),
            (registro[0], registro[1].isoformat(), float(registro[2]), registro[3],  registro[4], registro[5], registro[6])
            )) for registro in result]))

#=======================================================servicio_venta================================================================

@gets.get("/servicio-venta",tags=["Servicio-Venta"], response_model=List[ServicioVenta])
def allfactura():
    with engine.connect() as conn:
        result = conn.execute(servicio_venta.select().where(servicio_venta.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'id_servicio', 'cantidad','subtotal'),
            (registro[0], registro[1], registro[2],float(registro[3]))
            )) for registro in result]))

@gets.get("/servicio-venta/{id}",tags=["Servicio-Venta"], response_model=List[ServicioVenta])
def verServicioVenta(id:int):
    with engine.connect() as conn:
        result = conn.execute(servicio_venta.select().where(and_(servicio_venta.c.deleted_at == None, servicio_venta.c.id_factura == id))).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'id_servicio', 'cantidad','subtotal'),
            (registro[0], registro[1], registro[2],float(registro[3]))
            )) for registro in result]))

#=======================================================ProductoVenta================================================================

@gets.get("/producto-venta",tags=["Producto-Venta"], response_model=List[ProductoVenta])
def allfactura():
    with engine.connect() as conn:
        result = conn.execute(producto_venta.select().where(producto_venta.c.deleted_at == None)).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'id_producto', 'cantidad','subtotal'),
            (registro[0], registro[1], registro[2],float(registro[3]))
            )) for registro in result]))

@gets.get("/producto-venta/{id}",tags=["Producto-Venta"], response_model=List[ProductoVenta])
def verProductoVenta(id:int):
    with engine.connect() as conn:
        result = conn.execute(producto_venta.select().where(and_(producto_venta.c.deleted_at == None, producto_venta.c.id_factura == id))).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_factura', 'id_producto', 'cantidad','subtotal'),
            (registro[0], registro[1], registro[2],float(registro[3]))
            )) for registro in result]))

