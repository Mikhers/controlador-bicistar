from pydantic import BaseModel
from typing import Optional, Set
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


class Pedido(BaseModel):
    id_pedido: Optional[int]
    fecha_realizado: Optional[datetime]
    fecha_llegada: Optional[datetime]
    estado_pedido: Set[str] = {"en proceso","recibido"}
    total_pedido: Optional[float]
    id_sede: Optional[int]
    id_proveedor: Optional[int]


class Empleado(BaseModel):
    id_empleado: Optional[int]
    nombre_empleado: str
    apellido_empleado: Optional[str]
    email_empleado: str
    password_empleado: str
    permiso_empleado: Set[str] = {"ALL PRIVILEGES", "CREATE", "DROP", "DELETE","INSERT"}
    rol_empleado: Set[str] = {"administrador","caja","root"}
    salario_empleado: int
    sede: int


class CategoriaProducto(BaseModel):
    id_categoria_producto: Optional[int]
    nombre_categoria_producto: str
    descripcion_categoria_producto: str


class Producto(BaseModel):
    id_producto: Optional[int]
    nombre_producto: str
    descripcion_producto: Optional[str]
    precio_producto: float
    cantidad_producto: Optional[int]
    stock: Optional[int]
    codigo_producto: Optional[int]
    id_categoria_producto: Optional[int]


class PedidoProducto(BaseModel):
    id_pedido: Optional[int]
    id_producto: int
    cantidad_producto: int
    precio_unitario: int


class CategoriaServicio(BaseModel):
    id_categoria_servicio: Optional[int]
    nombre_servicio: str
    descripcion_servicio: str


class Cliente(BaseModel):
    id_cliente: Optional[int]
    nombre_cliente: str
    apellido_cliente: Optional[str]
    telefono_cliente: Optional[str]
    email_cliente: Optional[str]
    cc_cliente: Optional[str]
    direccion_cliente: Optional[str]


class Servicio(BaseModel):
    id_servicio: Optional[int]
    descripcion_servicio: Optional[str]
    fecha_servicio: Optional[datetime]
    precio_servicio: float
    id_empleado: int
    id_categoria_servicio: int
    id_cliente: int


class Venta(BaseModel):
    id_venta: Optional[int]
    fecha_venta: Optional[datetime]
    descripcion_venta: Optional[str]
    precio_venta: float
    id_empleado: int
    id_producto: int
    id_cliente: int
