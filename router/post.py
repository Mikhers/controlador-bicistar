from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.schemaTablas import Sede, Proveedor, Pedidos, Empleado, CategoriaProducto, Productos, PedidoProducto, CategoriaServicio, Clientes, Servicios,SedesProductos,Factura,ServicioVenta,ProductoVenta
from model.modelBicistar import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios,sedes_productos,factura,servicio_venta,producto_venta
from werkzeug.security import generate_password_hash#, check_password_hash
from config.db import engine
from typing import List
import json

posts = APIRouter(
    prefix = "/new"
)

#=======================================================SEDE================================================================
@posts.post("/sede", tags=["Sedes"], status_code=HTTP_201_CREATED)
def insertSede(data: Sede):
    with engine.connect() as conn:
        conn.execute(sede.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#=======================================================proveedor================================================================
@posts.post("/proveedor", tags=["Proveedores"], status_code=HTTP_201_CREATED)
def insertProveedor(data: Proveedor):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(proveedor.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
  #=======================================================EMPLEADOS================================================================  
@posts.post("/empleado", tags=["Empleados"], status_code=HTTP_201_CREATED)
def insertEmpleado(data: Empleado):
    with engine.connect() as conn:
        new_data=data.dict()
        new_data['password_empleado'] = generate_password_hash(data.password_empleado, "pbkdf2:sha256:30",30)
        conn.execute(empleado.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#=======================================================PEDIDOS================================================================
@posts.post("/pedido", tags=["Pedidos"])
def insertPedido(data: Pedidos):
    with engine.connect() as conn:
        resul=conn.execute(pedidos.select()).fetchall()
        idMax=0
        for res in resul: 
            if idMax < res[0]: idMax=res[0]
        new_data=data.dict()
        new_data['id_pedido']=idMax + 1
        conn.execute(pedidos.insert().values(new_data))
        conn.commit()

        return {"id_pedido":idMax+1}
    


#=======================================================CATEGORIA-PRODUCTO================================================================
@posts.post("/categoria-producto", tags=["Categoria-producto"], status_code=HTTP_201_CREATED)
def insertCategoriaProducto(data: CategoriaProducto):
    with engine.connect() as conn:
        conn.execute(categoria_producto.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


#=======================================================Productos================================================================
#FUNCION PARA CODIGO DE BARRAS
def validarIDProducto(data: Productos):
    with engine.connect() as conn:
        new_data = data.dict()
        result = conn.execute(productos.select()).fetchall()
        dicio = json.loads(json.dumps([dict(zip(
            ('id_producto', 'nombre_producto', 'descripcion_producto', 'precio_producto','codigo_producto','id_categoria_producto'),
            (registro[0], registro[1], registro[2], float(registro[3]), registro[4], registro[5])
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

@posts.post("/producto", tags=["Productos"], status_code=HTTP_201_CREATED)
def insertProducto(data: list[Productos]):
    with engine.connect() as conn:
        for index in data:
            new_data = validarIDProducto(index)
            conn.execute(productos.insert().values(new_data))
            conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    
#=======================================================sedes-productos================================================================

@posts.post("/sedes-productos", tags=["Sedes-Productos"], status_code=HTTP_201_CREATED)
def insertPedido(data: SedesProductos):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(sedes_productos.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


#=======================================================PEDIDO-PRODUCTO================================================================
@posts.post("/pedido-producto", tags=["Pedido-producto"], status_code=HTTP_201_CREATED)
def insertPedidoProducto(data: PedidoProducto):
    with engine.connect() as conn:
        new_data=data.dict()
        conn.execute(pedido_producto.insert().values(new_data))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    
#=======================================================CategoriaServicio================================================================
@posts.post("/categoria-servicio", tags=["Categoria-servicio"], status_code=HTTP_201_CREATED)
def insertCategoriaServicio(data: CategoriaServicio):
    with engine.connect() as conn:
        conn.execute(categoria_servicio.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)


#=======================================================SERVICIOS================================================================
@posts.post("/servicio", tags=["Servicios"], status_code=HTTP_201_CREATED)
def insertServicios(data: Servicios):
    with engine.connect() as conn:
        conn.execute(servicios.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

#=======================================================CLIENTES================================================================
@posts.post("/cliente", tags=["Clientes"], status_code=HTTP_201_CREATED)
def insertCliente(data: Clientes):
    with engine.connect() as conn:
        conn.execute(clientes.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    

#=======================================================Factura================================================================
def codigoBarrasFactura(data: Factura):
   with engine.connect() as conn:
        new_data = data.dict()
        result = conn.execute(factura.select()).fetchall()
        dicio = json.loads(json.dumps([dict(zip(
            ('id_factura', 'fecha_factura', 'total','codigo_factura','id_empleado','cc_cliente','id_sede'),
            (registro[0], registro[1].isoformat(), float(registro[2]), registro[3],  registro[4], registro[5], registro[6])
            )) for registro in result]))
        max_id=0
        for facturaa in dicio:
            # Obtener el valor de la clave 'id_factura'
            id_factura = facturaa['id_factura']
            # Si el valor de 'id_factura' es mayor que el número mayor actual, actualizar la variable 'max_id'
            if id_factura > max_id:
                max_id = id_factura

        if(data.id_factura != None):
            num = data.id_factura
        else:
            num = max_id+1
            new_data['id_factura'] = num

        if(len(str(num))<2):
            new_data['codigo_factura'] = "90000000000"+str(num)
        elif(len(str(num))<3):
            new_data['codigo_factura'] = "9000000000"+str(num)
        elif(len(str(num))<4):
            new_data['codigo_factura'] = "900000000"+str(num)
        elif(len(str(num))<5):
            new_data['codigo_factura'] = "90000000"+str(num)
        elif(len(str(num))<6):
            new_data['codigo_factura'] = "9000000"+str(num)
        elif(len(str(num))<7):
            new_data['codigo_factura'] = "900000"+str(num)
        elif(len(str(num))<8):
            new_data['codigo_factura'] = "90000"+str(num)
        elif(len(str(num))<9):
            new_data['codigo_factura'] = "9000"+str(num)
        elif(len(str(num))<10):
            new_data['codigo_factura'] = "900"+str(num)
        elif(len(str(num))<11):
            new_data['codigo_factura'] = "90"+str(num)
        elif(len(str(num))<12):
            new_data['codigo_factura'] = "9"+str(num)
        return new_data

@posts.post("/factura", tags=["Facturas"],status_code=HTTP_201_CREATED)
def insertfactura(data: Factura):
    with engine.connect() as conn:
        new_data = codigoBarrasFactura(data)
        conn.execute(factura.insert().values(new_data))
        conn.commit()
        return new_data["id_factura"]
    

#=======================================================servicio_venta================================================================
@posts.post("/servicio-venta", tags=["Servicio-Venta"], status_code=HTTP_201_CREATED)
def insertServicioVenta(data: ServicioVenta):
    with engine.connect() as conn:
        conn.execute(servicio_venta.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)
    
#=======================================================producto_venta================================================================
@posts.post("/producto-venta", tags=["Producto-Venta"], status_code=HTTP_201_CREATED)
def insertProductoVenta(data: ProductoVenta):
    with engine.connect() as conn:
        conn.execute(producto_venta.insert().values(data.dict()))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)



