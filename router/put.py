from fastapi import APIRouter
from sqlalchemy import and_
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios,SedesProductos, Factura,ServicioVenta,ProductoVenta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios,sedes_productos,factura,servicio_venta,producto_venta
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
import json

puts = APIRouter(
    prefix = "/modify"
)


#=======================================================SEDE================================================================
@puts.put("/sede/{id}",tags=["Sedes"], response_model=Sede)
def alterSede(data: Sede, id: int):
    with engine.connect() as conn:
        conn.execute(sede.update().values(
                                        nombre_sede=data.nombre_sede,
                                        direccion_sede=data.direccion_sede,
                                        ciudad_sede=data.ciudad_sede
        ).where(sede.c.id_sede == id))
        conn.commit()
        result = conn.execute(sede.select().where(sede.c.id_sede == id)).first()
        return {"id_sede":result[0], "nombre_sede":result[1], "direccion_sede":result[2], "ciudad_sede":result[3]}


#=======================================================proveedor================================================================
@puts.put("/proveedor/{id}",tags=["Proveedores"], response_model=Proveedor)
def alterProveedor(data: Proveedor, id: int):
    with engine.connect() as conn:
        conn.execute(proveedor.update().values(
                                        nombre_proveedor=data.nombre_proveedor,
                                        direccion_proveedor=data.direccion_proveedor,
                                        telefono_proveedor=data.telefono_proveedor,
                                        email_proveedor=data.email_proveedor

        ).where(proveedor.c.id_proveedor == id))
        conn.commit()
        result = conn.execute(proveedor.select().where(proveedor.c.id_proveedor == id)).first()
        return {"id_proveedor":result[0], "nombre_proveedor":result[1], "direccion_proveedor":result[2], "telefono_proveedor":result[3],"email_proveedor":result[4]}

#=======================================================EMPLEADOS================================================================
@puts.put("/empleado/{id}",tags=["Empleados"], response_model=Empleado)
def alterEmpleado(data: Empleado, id: int):
    with engine.connect() as conn:
        encryp = generate_password_hash(data.password_empleado, "pbkdf2:sha256:30",30)
        conn.execute(empleado.update().values(
                                        nombre_empleado=data.nombre_empleado,
                                        apellido_empleado=data.apellido_empleado,
                                        email_empleado=data.email_empleado,
                                        password_empleado=encryp,
                                        permiso_empleado=data.permiso_empleado,
                                        rol_empleado=data.rol_empleado,
                                        salario_empleado=data.salario_empleado,
                                        id_sede=data.id_sede
        ).where(empleado.c.id_empleado == id))
        conn.commit()
        result = conn.execute(empleado.select().where(empleado.c.id_empleado == id)).first()
        return {"id_empleado":result[0], "nombre_empleado":result[1], "apellido_empleado":result[2], "email_empleado":result[3],"password_empleado":result[4],
                "permiso_empleado":result[5],"rol_empleado":result[6],"salario_empleado": result[7],"id_sede":result[8]}
# #=======================================================PEDIDOS================================================================
@puts.put("/pedido/{id}",tags=["Pedidos"], response_model=Pedidos)
def alterPedidos(data: Pedidos, id: int):
    with engine.connect() as conn:
        conn.execute(pedidos.update().values(
                                    fecha_realizado=data.fecha_realizado,
                                    fecha_llegada=data.fecha_llegada,
                                    estado_pedido=data.estado_pedido,
                                    total_pedido=data.total_pedido,
                                    id_proveedor=data.id_proveedor,
                                    id_empleado=data.id_empleado,
                                    id_sede=data.id_sede
        ).where(pedidos.c.id_pedido == id))
        conn.commit()
        result = conn.execute(pedidos.select().where(pedidos.c.id_pedido == id)).first()
        return {"id_pedido":result[0], "fecha_realizado":result[1], "fecha_llegada":result[2], "estado_pedido":result[3],"total_pedido":result[4],"id_sede":result[5],"id_proveedor":result[6],'id_empleado':result[7]}


# #=======================================================CATEGORIA-PRODUCTO================================================================
@puts.put("/categoria-producto/{id}",tags=["Categoria-producto"], response_model=CategoriaProducto)
def alterCategoriaProducto(data: CategoriaProducto, id: int):
    with engine.connect() as conn:
        conn.execute(categoria_producto.update().values(
                                            nombre_categoria_producto=data.nombre_categoria_producto,
                                            descripcion_categoria_producto=data.descripcion_categoria_producto
        ).where(categoria_producto.c.id_categoria_producto == id))
        conn.commit()
        result = conn.execute(categoria_producto.select().where(categoria_producto.c.id_categoria_producto == id)).first()
        return {"id_categoria_producto":result[0], "nombre_categoria_producto":result[1], "descripcion_categoria_producto":result[2]}

# #=======================================================Productos================================================================
#FUNCION PARA CODIGO DE BARRAS

@puts.put("/producto/{id}",tags=["Productos"], response_model=Productos)
def alterProductos(data: Productos, id: int):
    with engine.connect() as conn:
        conn.execute(productos.update().values(
                                        nombre_producto=data.nombre_producto,
                                        descripcion_producto=data.descripcion_producto,
                                        precio_producto=data.precio_producto,
                                        id_categoria_producto=data.id_categoria_producto,

        ).where(productos.c.id_producto == id))
        conn.commit()
        result = conn.execute(productos.select().where(productos.c.id_producto == id)).first()
        return {"id_producto":result[0], "nombre_producto":result[1], "descripcion_producto":result[2], "precio_producto":result[3],"codigo_producto":result[4],"id_categoria_producto": result[5]}

#=======================================================sedes-productos================================================================
@puts.put("/sedes-productos/{id}/{idd}", tags=["Sedes-Productos"], response_model=SedesProductos)
def alterCategoriaProducto(data: SedesProductos, id: int, idd: int):
    with engine.connect() as conn:
        conn.execute(sedes_productos.update().values(
                                            id_sede=data.id_sede,
                                            id_producto=data.id_producto,
                                            stock=data.stock
        ).where(and_(sedes_productos.c.id_sede == id, sedes_productos.c.id_producto == idd)))
        conn.commit()
        result = conn.execute(sedes_productos.select().where(and_(sedes_productos.c.id_sede == id, sedes_productos.c.id_producto == idd))).first()
        return {"id_sede":result[0], "id_producto":result[1], "stock":result[2]}


# #=======================================================PEDIDO-PRODUCTO================================================================
@puts.put("/pedido-producto/{id}/{idd}",tags=["Pedido-producto"], response_model=PedidoProducto)
def alterPedidoProducto(data: PedidoProducto, id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(pedido_producto.update().values(
                                            id_pedido=data.id_pedido,
                                            id_producto=data.id_producto,
                                            cantidad_producto=data.cantidad_producto,
                                            precio_unitario=data.precio_unitario

        ).where(and_(pedido_producto.c.id_pedido == id, pedido_producto.c.id_producto == idd)))
        conn.commit()
        result = conn.execute(pedido_producto.select().where(and_(pedido_producto.c.id_pedido == id, pedido_producto.c.id_producto == idd))).first()
        return {"id_pedido":result[0], "id_producto":result[1], "cantidad_producto":result[2], "precio_unitario":result[3]}

# #=======================================================CategoriaServicio================================================================
@puts.put("/categoria-servicio/{id}",tags=["Categoria-servicio"], response_model=CategoriaServicio)
def alterCategoriaServicio(data: CategoriaServicio, id: int):
    with engine.connect() as conn:
        conn.execute(categoria_servicio.update().values(
                                            nombre_servicio=data.nombre_servicio,
                                            descripcion_servicio=data.descripcion_servicio
                                            
        ).where(categoria_servicio.c.id_categoria_servicio == id))
        conn.commit()
        result = conn.execute(categoria_servicio.select().where(categoria_servicio.c.id_categoria_servicio == id)).first()
        return {"id_categoria_servicio":result[0], "nombre_servicio":result[1], "descripcion_servicio":result[2]}

#=======================================================SERVICIOS================================================================
@puts.put("/servicios/{id}",tags=["Servicios"], response_model=Servicios)
def alterServicios(data: Servicios, id: int):
    with engine.connect() as conn:
        conn.execute(servicios.update().values(
                                        nombre_servicio=data.nombre_servicio,
                                        descripcion_servicio=data.descripcion_servicio,
                                        precio_servicio=data.precio_servicio,
                                        id_categoria_servicio=data.id_categoria_servicio,

        ).where(servicios.c.id_servicio == id))
        conn.commit()
        result = conn.execute(servicios.select().where(servicios.c.id_servicio == id)).first()
        return {"id_servicio":result[0], "nombre_servicio":result[1],"descripcion_servicio":result[2], "precio_servicio":result[3],
                "id_categoria_servicio":result[4]}

# #=======================================================CLIENTES================================================================
@puts.put("/cliente/{id}",tags=["Clientes"], response_model=Clientes)
def alterClientes(data: Clientes, id: int):
    with engine.connect() as conn:
        conn.execute(clientes.update().values(
                                        nombre_cliente=data.nombre_cliente,
                                        apellido_cliente=data.apellido_cliente,
                                        telefono_cliente=data.telefono_cliente,
                                        email_cliente=data.email_cliente,
                                        cc_cliente=data.cc_cliente,
                                        direccion_cliente=data.direccion_cliente
                                            
        ).where(clientes.c.cc_cliente == id))
        conn.commit()
        result = conn.execute(clientes.select().where(clientes.c.cc_cliente == id)).first()
        return {"cc_cliente":result[0], "nombre_cliente":result[1], "apellido_cliente":result[2], "telefono_cliente":result[3],"email_cliente":result[4],
                "direccion_cliente":result[5]}


# #=======================================================factura================================================================
@puts.put("/factura/{id}",tags=["Facturas"], response_model=Factura)
def alterFactura(data: Factura, id: int):
    with engine.connect() as conn:
        conn.execute(factura.update().values(
                                    fecha_factura=data.fecha_factura,
                                    total=data.total,
                                    codigo_factura=data.codigo_factura,
                                    id_empleado=data.id_empleado,
                                    cc_cliente=data.cc_cliente,
                                    id_sede=data.id_sede

        ).where(factura.c.id_factura == id))
        conn.commit()
        result = conn.execute(factura.select().where(factura.c.id_factura == id)).first()
        return {"id_factura":result[0], "fecha_factura":result[1], "total":result[2], "codigo_factura":result[3],"id_empleado":result[4],
                "cc_cliente":result[5],"id_sede":result[6]}
    

# #=======================================================Servicio-Venta================================================================

@puts.put("/servicio-venta/{id}/{idd}",tags=["Servicio-Venta"], response_model=ServicioVenta)
def alterServicioVenta(data: ServicioVenta, id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(servicio_venta.update().values(
                                    id_factura=data.id_factura,
                                    id_servicio=data.id_servicio,
                                    cantidad=data.cantidad,
                                    subtotal=data.subtotal

        ).where(and_(servicio_venta.c.id_factura == id,servicio_venta.c.id_servicio == idd)))
        conn.commit()
        result = conn.execute(servicio_venta.select().where(servicio_venta.c.id_factura == id)).first()
        return {"id_factura":result[0], "id_servicio":result[1], "cantidad":result[2], "subtotal":result[3]}
    
# #=======================================================Servicio-Venta================================================================

@puts.put("/producto-venta/{id}/{idd}",tags=["Producto-Venta"], response_model=ProductoVenta)
def alterProductoVenta(data: ProductoVenta, id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(producto_venta.update().values(
                                    id_factura=data.id_factura,
                                    id_producto=data.id_producto,
                                    cantidad=data.cantidad,
                                    subtotal=data.subtotal

        ).where(and_(producto_venta.c.id_factura == id,producto_venta.c.id_producto == idd)))
        conn.commit()
        result = conn.execute(producto_venta.select().where(producto_venta.c.id_factura == id)).first()
        return {"id_factura":result[0], "id_producto":result[1], "cantidad":result[2], "subtotal":result[3]}