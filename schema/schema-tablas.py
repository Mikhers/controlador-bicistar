from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class schemaSede(BaseModel):  # <---SEDE
    id: Optional[int]   
    nombre_sede: str
    direccion_sede: str 
    ciudad_sede: str

class schemaProveedor(BaseModel):  # <---PROVEEDORES
    id: Optional[int]
    nombre_proveedor: str
    direccion_proveedor: str
    telefono_proveedor: str
    email_proveedor: str

class schemaPedidos(BaseModel):  # <---PEDIDOS
    id: Optional[int]
    fecha_llegada: datetime #   <---datetime.now() asi se asigna
    estado_pedido: str
    total_pedido: float
    id_sede: int
    id_proveedor: int

class schemaEmpleado(BaseModel):  # <---EMPLEADOS
    id: Optional[int]
    nombre_empleado: str
    apellido_empleado:str
    email_empleado:str
    password_empleado:str
    permiso_empleado:str
    rol_empleado:str
    salario_empleado:float
    sede:int

class schemaCategoriaP(BaseModel):  # <---CATEGORIA DE PRODUCTOS
    id: Optional[int]
    nombre_categoria_producto: str
    descripcion_categoria_producto: str

class schemaProductos(BaseModel):  # <---PRODUCTOS
    id: Optional[int]
    nombre_producto: str
    descripcion_producto: str
    precio_producto: float
    cantidad_producto: int
    stock: int
    codigo_producto: int
    id_categoria_producto: int

class schemaPedidoP(BaseModel):  # <---PEDIDO_PRODUCTO
    id: Optional[int]
    id_pedido: int
    id_producto: int
    cantidad_producto: int
    precio_unitario: float

class schemaCategoriaS(BaseModel):  # <---CATEGORIAS DE SERVICIOS
    id: Optional[int]
    nombre_servicio: str
    descripcion_servicio: str

class schemaClientes(BaseModel):  # <---CLIENTES
    id: Optional[int]
    nombre_cliente: str
    apellido_cliente: str
    telefono_cliente: str
    email_cliente: str
    cc_cliente: str
    direccion_cliente: str

class schemaServicios(BaseModel):  # <---SERVICIOS
    id: Optional[int]
    descripcion_servicio: str
    fecha_servicio: datetime
    precio_servicio: float
    id_empleado: int
    id_categoria_servicio: int
    id_cliente: int

class schemaVentas(BaseModel):  # <---VENTAS
    id: Optional[int]
    fecha_venta: datetime
    descripcion_venta: str
    precio_venta: int
    id_empleado: int
    id_producto: int
    id_cliente: int