from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios, Venta
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios, venta
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
from typing import List
import json

bicistar = APIRouter()



@bicistar.get("/",tags=["Documentación"])
def root():
    return {"message": "Hola, Soy la API de BiciStar"}



#=======================================================SEDE================================================================
#METODO GET
@bicistar.get("/ver-sedes",tags=["Sedes"], response_model=List[Sede])
def allSede():
    with engine.connect() as conn:
        result = conn.execute(sede.select()).fetchall()
        return json.loads(json.dumps([dict(zip(('id_sede', 'nombre_sede', 'direccion_sede', 'ciudad_sede'), registro)) for registro in result])) 

#METODO POST
@bicistar.post("/insert-sede", tags=["Sedes"], status_code=HTTP_201_CREATED)
def insertSede(data: Sede):
    with engine.connect() as conn:
        conn.execute(sede.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-sede/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Sedes'])
def dropSede(id: int):
    with engine.connect() as conn:
        conn.execute(sede.delete().where(sede.c.id_sede == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================proveedor================================================================
#METODO GET
@bicistar.get("/ver-proveedores",tags=["Proveedores"], response_model=List[Proveedor])
def allProveedores():
    with engine.connect() as conn:
        result = conn.execute(proveedor.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_proveedor', 'nombre_proveedor', 'direccion_proveedor', 'telefono_proveedor','email_proveedor'), 
            registro)) for registro in result]))

#METODO POST
@bicistar.post("/insert-new-proveedor", tags=["Proveedores"], status_code=HTTP_201_CREATED)
def insertProveedor(data: Proveedor):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(proveedor.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-proveedor/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Proveedores'])
def dropProveedor(id: int):
    with engine.connect() as conn:
        conn.execute(proveedor.delete().where(proveedor.c.id_proveedor == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================PEDIDOS================================================================
#METODO GET
@bicistar.get("/ver-pedidos",tags=["Pedidos"], response_model=List[Pedidos])
def allPedidos():
    with engine.connect() as conn:
        result = conn.execute(pedidos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido', 'fecha_realizado', 'fecha_llegada', 'estado_pedido','total_pedido','id_sede','id_proveedor'),
            (registro[0], registro[1].isoformat(), registro[2].isoformat(), str(registro[3]), float(registro[4]), registro[5], registro[6])
            )) for registro in result]))
    
#METODO POST
@bicistar.post("/insert-new-pedido", tags=["Pedidos"], status_code=HTTP_201_CREATED)
def insertPedido(data: Pedidos):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(pedidos.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-pedido/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Pedidos'])
def dropPedido(id: int):
    with engine.connect() as conn:
        conn.execute(pedidos.delete().where(pedidos.c.id_pedido == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================EMPLEADOS================================================================
#METODO GET
@bicistar.get("/ver-empleados",tags=["Empleados"], response_model=List[Empleado])
def allEmpleados():
    with engine.connect() as conn:
        result = conn.execute(empleado.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_empleado', 'nombre_empleado', 'apellido_empleado', 'email_empleado','password_empleado','permiso_empleado','rol_empleado','salario_empleado','sede'),
            (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], float(registro[7]), registro[8])
            )) for registro in result]))
    
#METODO POST
@bicistar.post("/insert-new-empleado", tags=["Empleados"], status_code=HTTP_201_CREATED)
def insertEmpleado(data: Empleado):
    with engine.connect() as conn:
        new_data=data.dict()
        new_data['password_empleado'] = generate_password_hash(data.password_empleado, "pbkdf2:sha256:30",30)
        conn.execute(empleado.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-empleado/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Empleados'])
def dropEmpleados(id: int):
    with engine.connect() as conn:
        conn.execute(empleado.delete().where(empleado.c.id_empleado == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================CATEGORIA-PRODUCTO================================================================
#METODO GET
@bicistar.get("/ver-categoria-producto",tags=["Categoria-producto"], response_model=List[CategoriaProducto])
def allCategoriaProducto():
    with engine.connect() as conn:
        result = conn.execute(categoria_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_producto', 'nombre_categoria_producto', 'descripcion_categoria_producto'),
            registro)) for registro in result]))

#METODO POST
@bicistar.post("/insert-new-categoria-producto", tags=["Categoria-producto"], status_code=HTTP_201_CREATED)
def insertCategoriaProducto(data: CategoriaProducto):
    with engine.connect() as conn:
        conn.execute(categoria_producto.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-categoria-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-producto'])
def dropCategoriaProducto(id: int):
    with engine.connect() as conn:
        conn.execute(categoria_producto.delete().where(categoria_producto.c.id_categoria_producto == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================SEDE================================================================
#METODO GET
@bicistar.get("/ver-productos",tags=["Productos"], response_model=List[Productos])
def allProductos():
    with engine.connect() as conn:
        result = conn.execute(productos.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','cantidad_producto','stock','codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], registro[6], registro[7])
            )) for registro in result]))

#FUNCION PARA CODIGO DE BARRAS
def validarIDProducto():
    with engine.connect() as conn:
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
        
        return max_id
#METODO POST
@bicistar.post("/insert-new-producto", tags=["Productos"], status_code=HTTP_201_CREATED)
def insertProducto(data: Productos):
    with engine.connect() as conn:
        max_id = validarIDProducto()
        new_data = data.dict()
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
        
        conn.execute(productos.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Productos'])
def dropProducto(id: int):
    with engine.connect() as conn:
        conn.execute(productos.delete().where(productos.c.id_producto == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================PEDIDO-PRODUCTO================================================================
#METODO GET
@bicistar.get("/ver-pedido-producto",tags=["Pedido-producto"], response_model=List[PedidoProducto])
def allPedidoProducto():
    with engine.connect() as conn:
        result = conn.execute(pedido_producto.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_pedido_producto','id_pedido', 'id_producto', 'cantidad_producto','precio_unitario'),
            (registro[0], registro[1], registro[2], registro[3], float(registro[4]))
            )) for registro in result]))
 
#METODO POST
@bicistar.post("/insert-new-pedido-producto", tags=["Pedido-producto"], status_code=HTTP_201_CREATED)
def insertPedidoProducto(data: PedidoProducto):
    with engine.connect() as conn:
        conn.execute(pedido_producto.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-pedido-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Pedido-producto'])
def dropPedidoProducto(id: int):
    with engine.connect() as conn:
        conn.execute(pedido_producto.delete().where(pedido_producto.c.id_pedido_producto == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================CategoriaServicio================================================================
#METODO GET
@bicistar.get("/ver-categoria-servicio",tags=["Categoria-servicio"], response_model=List[CategoriaServicio])
def allCategoriaServicio():
    with engine.connect() as conn:
        result = conn.execute(categoria_servicio.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_categoria_servicio', 'nombre_servicio', 'descripcion_servicio'),
            registro)) for registro in result]))

#METODO POST
@bicistar.post("/insert-new-categoria-servicio", tags=["Categoria-servicio"], status_code=HTTP_201_CREATED)
def insertCategoriaServicio(data: CategoriaServicio):
    with engine.connect() as conn:
        conn.execute(categoria_servicio.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-categoria-servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-servicio'])
def dropCategoriaServicio(id: int):
    with engine.connect() as conn:
        conn.execute(categoria_servicio.delete().where(categoria_servicio.c.id_categoria_servicio == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================CategoriaServicio================================================================
#METODO GET
@bicistar.get("/ver-clientes",tags=["Clientes"], response_model=List[Clientes])
def allClientes():
    with engine.connect() as conn:
        result = conn.execute(clientes.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_cliente', 'nombre_cliente', 'apellido_cliente','telefono_cliente','email_cliente','cc_cliente','direccion_cliente'),
            registro)) for registro in result]))
    
#METODO POST
@bicistar.post("/insert-new-cliente", tags=["Clientes"], status_code=HTTP_201_CREATED)
def insertCliente(data: Clientes):
    with engine.connect() as conn:
        conn.execute(clientes.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#METODO DELETE
@bicistar.delete("/delete-cliente/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Clientes'])
def dropClientes(id: int):
    with engine.connect() as conn:
        conn.execute(clientes.delete().where(clientes.c.id_cliente == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================SERVICIOS================================================================
#METODO GET
@bicistar.get("/ver-servicios",tags=["Servicios"], response_model=List[Servicios])
def allServicios():
    with engine.connect() as conn:
        result = conn.execute(servicios.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_servicio', 'descripcion_servicio', 'fecha_servicio','precio_servicio','id_empleado','id_categoria_servicio','id_cliente'),
            (registro[0], registro[1], registro[2].isoformat(), float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))
    
#METODO POST
@bicistar.post("/insert-new-servicio", tags=["Servicios"], status_code=HTTP_201_CREATED)
def insertServicios(data: Servicios):
    with engine.connect() as conn:
        conn.execute(servicios.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@bicistar.delete("/delete-servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Servicios'])
def dropServicios(id: int):
    with engine.connect() as conn:
        conn.execute(servicios.delete().where(servicios.c.id_servicio == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
#=======================================================SERVICIOS================================================================
#METODO GET
@bicistar.get("/ver-ventas",tags=["Ventas"], response_model=List[Venta])
def allVentas():
    with engine.connect() as conn:
        result = conn.execute(venta.select()).fetchall()
        return json.loads(json.dumps([dict(zip(
            ('id_venta', 'fecha_venta', 'descripcion_venta','precio_venta','id_empleado','id_producto','id_cliente'),
            (registro[0], registro[1].isoformat(), registro[2], float(registro[3]), registro[4], registro[5], registro[6])
            )) for registro in result]))

#METODO POST
@bicistar.post("/insert-new-venta", tags=["Ventas"], status_code=HTTP_201_CREATED)
def insertVenta(data: Venta):
    with engine.connect() as conn:
        conn.execute(venta.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    
#METODO DELETE
@bicistar.delete("/delete-ventas/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Ventas'])
def dropVenta(id: int):
    with engine.connect() as conn:
        conn.execute(venta.delete().where(venta.c.id_venta == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)


