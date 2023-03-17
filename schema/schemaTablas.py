# from dataclasses import Field
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Sede(BaseModel):
    id_sede: Optional[int]
    nombre_sede: str
    direccion_sede: str
    ciudad_sede: str


class Proveedor(BaseModel):
    id_proveedor: Optional[int]
    nombre_proveedor: str
    direccion_proveedor: Optional[str]
    telefono_proveedor: Optional[str]
    email_proveedor: Optional[str]


class Pedidos(BaseModel):
    id_pedido: Optional[int]
    fecha_realizado: Optional[datetime] = datetime.now()
    fecha_llegada: datetime
    estado_pedido: str
    total_pedido: float
    id_sede: int
    id_proveedor: int


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


class CategoriaProducto(BaseModel):
    id_categoria_producto: Optional[int]
    nombre_categoria_producto: str
    descripcion_categoria_producto: str


class Productos(BaseModel):      
    id_producto: Optional[int]
    nombre_producto: str
    descripcion_producto: Optional[str]
    precio_producto: float
    cantidad_producto: Optional[int] = 0
    stock: Optional[int]
    codigo_producto: Optional[int]
    id_categoria_producto: Optional[int]

    
class PedidoProducto(BaseModel):
    id_pedido: int
    id_producto: int
    cantidad_producto: int
    precio_unitario: float


class CategoriaServicio(BaseModel):
    id_categoria_servicio: Optional[int]
    nombre_servicio: str
    descripcion_servicio: str


class Clientes(BaseModel):
    id_cliente: Optional[int]
    nombre_cliente: str
    apellido_cliente: Optional[str]
    telefono_cliente: Optional[str]
    email_cliente: Optional[str]
    cc_cliente: Optional[str]
    direccion_cliente: Optional[str]


class Servicios(BaseModel):
    id_servicio: Optional[int]
    descripcion_servicio: Optional[str]
    fecha_servicio: Optional[datetime] = datetime.now()
    precio_servicio: float
    id_empleado: int
    id_categoria_servicio: int
    id_cliente: int


class Venta(BaseModel):
    id_venta: Optional[int]
    fecha_venta: Optional[datetime] = datetime.now()
    descripcion_venta: Optional[str]
    precio_venta: float
    id_empleado: int
    id_producto: int
    id_cliente: int
