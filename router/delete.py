from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime
from sqlalchemy import and_
from model.modelBicistar  import sede, proveedor, pedidos, empleado, categoria_producto, productos, pedido_producto, categoria_servicio, clientes, servicios,sedes_productos,factura,servicio_venta,producto_venta
from config.db import engine

deletes = APIRouter(
    prefix = "/delete"
)


#=======================================================SEDE================================================================
@deletes.delete("/sede/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Sedes'])
def dropSede(id: int):
    with engine.connect() as conn:
        conn.execute(sede.update().values(deleted_at=datetime.now()).where(sede.c.id_sede == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)


#=======================================================proveedor================================================================
@deletes.delete("/proveedor/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Proveedores'])
def dropProveedor(id: int):
    with engine.connect() as conn:
        conn.execute(proveedor.update().values(deleted_at=datetime.now()).where(proveedor.c.id_proveedor == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================EMPLEADOS================================================================
@deletes.delete("/empleado/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Empleados'])
def dropEmpleados(id: int):
    with engine.connect() as conn:
        conn.execute(empleado.update().values(deleted_at=datetime.now()).where(empleado.c.id_empleado == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================PEDIDOS================================================================
@deletes.delete("/pedido/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Pedidos'])
def dropPedido(id: int):
    with engine.connect() as conn:
        conn.execute(pedidos.update().values(deleted_at=datetime.now()).where(pedidos.c.id_pedido == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    

#=======================================================CATEGORIA-PRODUCTO================================================================
@deletes.delete("/categoria-producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-producto'])
def dropCategoriaProducto(id: int):
    with engine.connect() as conn:
        conn.execute(categoria_producto.update().values(deleted_at=datetime.now()).where(categoria_producto.c.id_categoria_producto == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    
#=======================================================Productos================================================================
@deletes.delete("/producto/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Productos'])
def dropProducto(id: int):
    with engine.connect() as conn:
        conn.execute(productos.update().values(deleted_at=datetime.now()).where(productos.c.id_producto == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================sedes-productos================================================================

@deletes.delete("/sedes-productos/{id}/{idd}", tags=["Sedes-Productos"], status_code=HTTP_204_NO_CONTENT)
def dropProducto(id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(sedes_productos.update().values(deleted_at=datetime.now()).where(and_(sedes_productos.c.id_sede == id, sedes_productos.c.id_producto == idd)))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================PEDIDO-PRODUCTO================================================================
@deletes.delete("/pedido-producto/{id}/{idd}", status_code=HTTP_204_NO_CONTENT, tags=['Pedido-producto'])
def dropPedidoProducto(id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(pedido_producto.update().values(deleted_at=datetime.now()).where(and_(pedido_producto.c.id_pedido == id, pedido_producto.c.id_producto == idd)))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================CategoriaServicio================================================================
@deletes.delete("/categoria-servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Categoria-servicio'])
def dropCategoriaServicio(id: int):
    with engine.connect() as conn:
        conn.execute(categoria_servicio.update().values(deleted_at=datetime.now()).where(categoria_servicio.c.id_categoria_servicio == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================SERVICIOS================================================================
@deletes.delete("/servicio/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Servicios'])
def dropServicios(id: int):
    with engine.connect() as conn:
        conn.execute(servicios.update().values(deleted_at=datetime.now()).where(servicios.c.id_servicio == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#=======================================================CLIENTES================================================================
@deletes.delete("/cliente/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Clientes'])
def dropClientes(id: int):
    with engine.connect() as conn:
        conn.execute(clientes.update().values(deleted_at=datetime.now()).where(clientes.c.id_cliente == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    
#=======================================================Venta================================================================
@deletes.delete("/factura/{id}", status_code=HTTP_204_NO_CONTENT, tags=['Facturas'])
def dropVenta(id: int):
    with engine.connect() as conn:
        conn.execute(factura.update().values(deleted_at=datetime.now()).where(factura.c.id_factura == id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    
#=======================================================ServicioVenta================================================================
@deletes.delete("/servicio-venta/{id}/{idd}",tags=["Servicio-Venta"], status_code=HTTP_204_NO_CONTENT)
def dropServicioVenta(id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(servicio_venta.update().values(deleted_at=datetime.now()).where(and_(servicio_venta.c.id_factura == id,servicio_venta.c.id_servicio == idd)))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
    
#=======================================================producto-venta================================================================
@deletes.delete("/producto-venta/{id}/{idd}",tags=["Producto-Venta"], status_code=HTTP_204_NO_CONTENT)
def dropServicioVenta(id: int, idd:int):
    with engine.connect() as conn:
        conn.execute(producto_venta.update().values(deleted_at=datetime.now()).where(and_(producto_venta.c.id_factura == id,producto_venta.c.id_producto == idd)))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)