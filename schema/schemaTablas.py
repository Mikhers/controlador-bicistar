# from dataclasses import Field
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Sede(BaseModel):
    id_sede: Optional[int]
    nombre_sede: str
    direccion_sede: str
    ciudad_sede: str
    deleted_at: Optional[datetime]


class Proveedor(BaseModel):
    id_proveedor: Optional[int]
    nombre_proveedor: str
    direccion_proveedor: Optional[str]
    telefono_proveedor: Optional[str]
    email_proveedor: Optional[str]
    deleted_at: Optional[datetime]


class Pedidos(BaseModel):
    id_pedido: Optional[int]
    fecha_realizado: Optional[datetime] = datetime.now()
    fecha_llegada: datetime
    estado_pedido: str
    total_pedido: float
    id_sede: int
    id_proveedor: int
    deleted_at: Optional[datetime]


class Empleado(BaseModel):
    id_empleado: Optional[int]
    nombre_empleado: str
    apellido_empleado: Optional[str]
    email_empleado: str
    password_empleado: str
    permiso_empleado: str
    rol_empleado: str
    salario_empleado: int
    sede: int
    deleted_at: Optional[datetime]


class CategoriaProducto(BaseModel):
    id_categoria_producto: Optional[int]
    nombre_categoria_producto: str
    descripcion_categoria_producto: str
    deleted_at: Optional[datetime]


class Productos(BaseModel):      
    id_producto: Optional[int]
    nombre_producto: str
    descripcion_producto: Optional[str]
    precio_producto: float
    codigo_producto: Optional[str]
    id_categoria_producto: Optional[int]
    deleted_at: Optional[datetime]

    
class PedidoProducto(BaseModel):
    id_pedido_producto: Optional[int]
    id_pedido: int
    id_producto: int
    cantidad_producto: int
    precio_unitario: float
    deleted_at: Optional[datetime]


class CategoriaServicio(BaseModel):
    id_categoria_servicio: Optional[int]
    nombre_servicio: str
    descripcion_servicio: str
    deleted_at: Optional[datetime]


class Clientes(BaseModel):
    id_cliente: Optional[int]
    nombre_cliente: str
    apellido_cliente: Optional[str]
    telefono_cliente: Optional[str]
    email_cliente: Optional[str]
    cc_cliente: Optional[str]
    direccion_cliente: Optional[str]
    deleted_at: Optional[datetime]


class Servicios(BaseModel):
    id_servicio: Optional[int]
    descripcion_servicio: Optional[str]
    fecha_servicio: Optional[datetime] = datetime.now()
    precio_servicio: float
    id_empleado: int
    id_categoria_servicio: int
    id_cliente: int
    deleted_at: Optional[datetime]


class Factura(BaseModel):
    id_factura: Optional[int]
    fecha_factura: Optional[datetime]
    total: float
    codigo_factura: Optional[str]
    id_empleado: int
    id_cliente: int
    id_sede: int
    deleted_at: Optional[datetime]

class ServicioVenta(BaseModel):
    id_factura: int
    id_servicio: int
    cantidad: int
    subtotal: float
    deleted_at: Optional[datetime]

class ProductoVenta(BaseModel):
    id_factura: int
    id_producto: int
    cantidad: int
    subtotal: float
    deleted_at: Optional[datetime]
