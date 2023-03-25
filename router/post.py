from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios
from model.modelBicistar import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
from typing import List
import json

posts = APIRouter(
    prefix = "/new"
)

#METODO POST
@posts.post("/sede", tags=["Sedes"], status_code=HTTP_201_CREATED)
def insertSede(data: Sede):
    with engine.connect() as conn:
        conn.execute(sede.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


@posts.post("/proveedor", tags=["Proveedores"], status_code=HTTP_201_CREATED)
def insertProveedor(data: Proveedor):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(proveedor.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    

# @posts.post("/pedido", tags=["Pedidos"], status_code=HTTP_201_CREATED)
# def insertPedido(data: Pedidos):
#     with engine.connect() as conn:
#         new_data=data.dict()
#         conn.execute(pedidos.insert().values(new_data))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)
    

# @posts.post("/empleado", tags=["Empleados"], status_code=HTTP_201_CREATED)
# def insertEmpleado(data: Empleado):
#     with engine.connect() as conn:
#         new_data=data.dict()
#         new_data['password_empleado'] = generate_password_hash(data.password_empleado, "pbkdf2:sha256:30",30)
#         conn.execute(empleado.insert().values(new_data))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)


# @posts.post("/categoria-producto", tags=["Categoria-producto"], status_code=HTTP_201_CREATED)
# def insertCategoriaProducto(data: CategoriaProducto):
#     with engine.connect() as conn:
#         conn.execute(categoria_producto.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)


# @posts.post("/pedido-producto", tags=["Pedido-producto"], status_code=HTTP_201_CREATED)
# def insertPedidoProducto(data: PedidoProducto):
#     with engine.connect() as conn:
#         conn.execute(pedido_producto.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)
    

# @posts.post("/categoria-servicio", tags=["Categoria-servicio"], status_code=HTTP_201_CREATED)
# def insertCategoriaServicio(data: CategoriaServicio):
#     with engine.connect() as conn:
#         conn.execute(categoria_servicio.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)

# #FUNCION PARA CODIGO DE BARRAS
# def validarIDProducto(data: Productos):
#     with engine.connect() as conn:
#         new_data = data.dict()
#         result = conn.execute(productos.select()).fetchall()
#         dicio = json.loads(json.dumps([dict(zip(
#             ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','cantidad_producto','stock','codigo_producto','id_categoria_producto'),
#             (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5], registro[6], registro[7])
#             )) for registro in result]))
#         max_id=0
#         for producto in dicio:
#             # Obtener el valor de la clave 'id_producto'
#             id_producto = producto['id_producto']
#             # Si el valor de 'id_producto' es mayor que el número mayor actual, actualizar la variable 'max_id'
#             if id_producto > max_id:
#                 max_id = id_producto

#         if(data.id_producto != None):
#             num = data.id_producto
#         else:
#             num = max_id+1
#             new_data['id_producto'] = num

#         if(len(str(num))<2):
#             new_data['codigo_producto'] = "10000000000"+str(num)
#         elif(len(str(num))<3):
#             new_data['codigo_producto'] = "1000000000"+str(num)
#         elif(len(str(num))<4):
#             new_data['codigo_producto'] = "100000000"+str(num)
#         elif(len(str(num))<5):
#             new_data['codigo_producto'] = "10000000"+str(num)
#         elif(len(str(num))<6):
#             new_data['codigo_producto'] = "1000000"+str(num)
#         elif(len(str(num))<7):
#             new_data['codigo_producto'] = "100000"+str(num)
#         elif(len(str(num))<8):
#             new_data['codigo_producto'] = "10000"+str(num)
#         elif(len(str(num))<9):
#             new_data['codigo_producto'] = "1000"+str(num)
#         elif(len(str(num))<10):
#             new_data['codigo_producto'] = "100"+str(num)
#         elif(len(str(num))<11):
#             new_data['codigo_producto'] = "10"+str(num)
#         elif(len(str(num))<12):
#             new_data['codigo_producto'] = "1"+str(num)
#         return new_data


# @posts.post("/producto", tags=["Productos"], status_code=HTTP_201_CREATED)
# def insertProducto(data: list[Productos]):
#     with engine.connect() as conn:
#         for index in data:

#             new_data = validarIDProducto(index)

#             conn.execute(productos.insert().values(new_data))
#             conn.commit()
#         return Response(status_code=HTTP_201_CREATED)



# @posts.post("/cliente", tags=["Clientes"], status_code=HTTP_201_CREATED)
# def insertCliente(data: Clientes):
#     with engine.connect() as conn:
#         conn.execute(clientes.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)
    

# @posts.post("/servicio", tags=["Servicios"], status_code=HTTP_201_CREATED)
# def insertServicios(data: Servicios):
#     with engine.connect() as conn:
#         conn.execute(servicios.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)


# @posts.post("/venta", tags=["Ventas"], status_code=HTTP_201_CREATED)
# def insertVenta(data: Venta):
#     with engine.connect() as conn:
#         conn.execute(venta.insert().values(data.dict()))
#         conn.commit()
#         return Response(status_code=HTTP_201_CREATED)



