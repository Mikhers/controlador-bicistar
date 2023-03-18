from fastapi import APIRouter
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios, Venta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios, venta
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
import json

puts = APIRouter(
    prefix = "/modify"
)


#METODO PUT
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


#METODO PUT
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

#METODO PUT
@puts.put("/pedido/{id}",tags=["Pedidos"], response_model=Pedidos)
def alterPedidos(data: Pedidos, id: int):
    with engine.connect() as conn:
        conn.execute(pedidos.update().values(
                                    fecha_realizado=data.fecha_realizado,
                                    fecha_llegada=data.fecha_llegada,
                                    estado_pedido=data.estado_pedido,
                                    total_pedido=data.total_pedido,
                                    id_sede=data.id_sede,
                                    id_proveedor=data.id_proveedor
        ).where(pedidos.c.id_pedido == id))
        conn.commit()
        result = conn.execute(pedidos.select().where(pedidos.c.id_pedido == id)).first()
        return {"id_pedido":result[0], "fecha_realizado":result[1], "fecha_llegada":result[2], "estado_pedido":result[3],"total_pedido":result[4],"id_sede":result[5],"id_proveedor":result[6]}

#METODO PUT
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
                                        sede=data.sede
        ).where(empleado.c.id_empleado == id))
        conn.commit()
        result = conn.execute(empleado.select().where(empleado.c.id_empleado == id)).first()
        return {"id_empleado":result[0], "nombre_empleado":result[1], "apellido_empleado":result[2], "email_empleado":result[3],"password_empleado":result[4],
                "permiso_empleado":result[5],"rol_empleado":result[6],"salario_empleado": result[7],"sede":result[8]}

#METODO PUT
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

#METODO PUT
@puts.put("/pedido-producto/{id}",tags=["Pedido-producto"], response_model=PedidoProducto)
def alterPedidoProducto(data: PedidoProducto, id: int):
    with engine.connect() as conn:
        conn.execute(pedido_producto.update().values(
                                            id_pedido=data.id_pedido,
                                            id_producto=data.id_producto,
                                            cantidad_producto=data.cantidad_producto,
                                            precio_unitario=data.precio_unitario

        ).where(pedido_producto.c.id_pedido_producto == id))
        conn.commit()
        result = conn.execute(pedido_producto.select().where(pedido_producto.c.id_pedido_producto == id)).first()
        return {"id_pedido_producto":result[0], "id_pedido":result[1], "id_producto":result[2], "cantidad_producto":result[3],"precio_unitario":result[4]}

#METODO PUT
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

#FUNCION PARA CODIGO DE BARRAS
def validarIDProducto(data: Productos):
    with engine.connect() as conn:
        new_data = data.dict()
        result = conn.execute(productos.select()).fetchall()
        dicio = json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','cantidad_producto','stock','codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], registro[6], registro[7])
            )) for registro in result]))
        max_id=0
        for producto in dicio:
            # Obtener el valor de la clave 'id_producto'
            id_producto = producto['id_producto']
            # Si el valor de 'id_producto' es mayor que el número mayor actual, actualizar la variable 'max_id'
            if id_producto > max_id:
                max_id = id_producto

        if(data.id_producto != None):
            num = data.id_producto
        else:
            num = max_id+1
            new_data['id_producto'] = num
   
        if(len(str(num))<2):
            new_data['codigo_producto'] = "10000000000"+str(num)
        elif(len(str(num))<3):
            new_data['codigo_producto'] = "1000000000"+str(num)
        elif(len(str(num))<4):
            new_data['codigo_producto'] = "100000000"+str(num)
        elif(len(str(num))<5):
            new_data['codigo_producto'] = "10000000"+str(num)
        elif(len(str(num))<6):
            new_data['codigo_producto'] = "1000000"+str(num)
        elif(len(str(num))<7):
            new_data['codigo_producto'] = "100000"+str(num)
        elif(len(str(num))<8):
            new_data['codigo_producto'] = "10000"+str(num)
        elif(len(str(num))<9):
            new_data['codigo_producto'] = "1000"+str(num)
        elif(len(str(num))<10):
            new_data['codigo_producto'] = "100"+str(num)
        elif(len(str(num))<11):
            new_data['codigo_producto'] = "10"+str(num)
        elif(len(str(num))<12):
            new_data['codigo_producto'] = "1"+str(num)
        return new_data

#METODO PUT
@puts.put("/producto/{id}",tags=["Productos"], response_model=Productos)
def alterProductos(data: Productos, id: int):
    with engine.connect() as conn:
        data.id_producto=id
        new_data = validarIDProducto(data)
        conn.execute(productos.update().values(
                                        nombre_producto=new_data["nombre_producto"],
                                        descripcion_producto=new_data["descripcion_producto"],
                                        precio_producto=new_data["precio_producto"],
                                        cantidad_producto=new_data["cantidad_producto"],
                                        stock=new_data["stock"],
                                        codigo_producto=new_data["codigo_producto"],
                                        id_categoria_producto=new_data["id_categoria_producto"]

        ).where(productos.c.id_producto == id))
        conn.commit()
        result = conn.execute(productos.select().where(productos.c.id_producto == id)).first()
        return {"id_producto":result[0], "nombre_producto":result[1], "descripcion_producto":result[2], "precio_producto":result[3],"cantidad_producto":result[4],
                "stock":result[5],"codigo_producto":result[6],"id_categoria_producto": result[7]}



#METODO PUT
@puts.put("/cliente/{id}",tags=["Clientes"], response_model=CategoriaServicio)
def alterClientes(data: Clientes, id: int):
    with engine.connect() as conn:
        conn.execute(clientes.update().values(
                                        nombre_cliente=data.nombre_cliente,
                                        apellido_cliente=data.apellido_cliente,
                                        telefono_cliente=data.telefono_cliente,
                                        email_cliente=data.email_cliente,
                                        cc_cliente=data.cc_cliente,
                                        direccion_cliente=data.direccion_cliente
                                            
        ).where(clientes.c.id_clientes == id))
        conn.commit()
        result = conn.execute(clientes.select().where(clientes.c.id_clientes == id)).first()
        return {"id_producto":result[0], "nombre_producto":result[1], "descripcion_producto":result[2], "precio_producto":result[3],"cantidad_producto":result[4],
                "stock":result[5],"codigo_producto":result[6]}

#METODO PUT
@puts.put("/servicios/{id}",tags=["Servicios"], response_model=Servicios)
def alterServicios(data: Servicios, id: int):
    with engine.connect() as conn:
        conn.execute(servicios.update().values(
                                       descripcion_servicio=data.descripcion_servicio,
                                        fecha_servicio=data.fecha_servicio,
                                        precio_servicio=data.precio_servicio,
                                        id_empleado=data.id_empleado,
                                        id_categoria_servicio=data.id_categoria_servicio,
                                        id_cliente=data.id_cliente
                                            
        ).where(servicios.c.id_servicio == id))
        conn.commit()
        result = conn.execute(servicios.select().where(servicios.c.id_servicio == id)).first()
        return {"id_servicio":result[0], "descripcion_servicio":result[1], "fecha_servicio":result[2], "precio_servicio":result[3],"id_empleado":result[4],
                "id_categoria_servicio":result[5],"id_cliente":result[6]}

#METODO PUT
@puts.put("/venta/{id}",tags=["Ventas"], response_model=Venta)
def alterVenta(data: Venta, id: int):
    with engine.connect() as conn:
        conn.execute(venta.update().values(
                                    fecha_venta=data.fecha_venta,
                                    descripcion_venta=data.descripcion_venta,
                                    precio_venta=data.precio_venta,
                                    id_empleado=data.id_empleado,
                                    id_producto=data.id_producto,
                                    id_cliente=data.id_cliente

        ).where(venta.c.id_venta == id))
        conn.commit()
        result = conn.execute(venta.select().where(venta.c.id_venta == id)).first()
        return {"id_venta":result[0], "fecha_venta":result[1], "descripcion_venta":result[2], "precio_venta":result[3],"id_empleado":result[4],
                "id_producto":result[5],"id_cliente":result[6]}