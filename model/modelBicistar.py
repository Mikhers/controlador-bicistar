from sqlalchemy import Table, Column, ForeignKey, null
from config.db import engine, meta_data
from sqlalchemy.sql.sqltypes import String,Integer, DateTime, DECIMAL
from datetime import datetime


sede = Table('sede', meta_data,
                    Column('id_sede', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_sede', String(50), nullable=False, unique=True),
                    Column('direccion_sede', String(255), nullable=False),
                    Column('ciudad_sede', String(255), nullable=False),
                    Column('deleted_at', DateTime, default=null)
)
# Definición de la tabla proveedor
proveedor = Table('proveedor', meta_data,
                    Column('id_proveedor', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_proveedor', String(50), nullable=False, unique=True),
                    Column('direccion_proveedor', String(100)),
                    Column('telefono_proveedor', String(20)),
                    Column('email_proveedor', String(255)),
                    Column('deleted_at', DateTime, default=null)
)

# Definición de la tabla empleado
empleado = Table('empleado', meta_data,
                    Column('id_empleado', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_empleado', String(50), nullable=False),
                    Column('apellido_empleado', String(50)),
                    Column('email_empleado', String(255), nullable=False),
                    Column('password_empleado', String(255), nullable=False),
                    Column('permiso_empleado', String(20)),
                    Column('rol_empleado', String(20)),
                    Column('salario_empleado', DECIMAL(10, 2)),
                    Column('id_sede', Integer, ForeignKey('sede.id_sede', ondelete='CASCADE', onupdate='CASCADE')),
                    Column('deleted_at', DateTime, default=null)
)

# Definición de la tabla pedidos
pedidos = Table('pedidos', meta_data,
                    Column('id_pedido', Integer, primary_key=True, autoincrement=True),
                    Column('fecha_realizado', DateTime,default=datetime.now),
                    Column('fecha_llegada', DateTime),
                    Column('estado_pedido', String(20), nullable=False),
                    Column('total_pedido', DECIMAL(10, 2)),
                    Column('id_sede', Integer, ForeignKey('sede.id_sede', ondelete='CASCADE', onupdate='CASCADE')),
                    Column('id_proveedor', Integer, ForeignKey('proveedor.id_proveedor', ondelete='CASCADE', onupdate='CASCADE')),
                    Column('id_empleado', Integer, ForeignKey('empleado.id_empleado', ondelete='CASCADE', onupdate='CASCADE')),
                    Column('deleted_at', DateTime, default=null)
)

# Definición de la tabla categoria_producto
categoria_producto = Table('categoria_producto', meta_data,
                    Column('id_categoria_producto', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_categoria_producto', String(50), nullable=False),
                    Column('descripcion_categoria_producto', String(300), nullable=False),
                    Column('deleted_at', DateTime, default=null)

)

# Definición de la tabla productos
productos = Table('productos', meta_data,
                    Column('id_producto', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_producto', String(100), nullable=False, unique=True),
                    Column('descripcion_producto', String(300)),
                    Column('precio_producto', DECIMAL(10, 2)),
                    Column('codigo_producto', String(50), nullable=False, unique=True),
                    Column('id_categoria_producto', Integer, ForeignKey('categoria_producto.id_categoria_producto', ondelete='CASCADE', onupdate='CASCADE')),
                    Column('deleted_at', DateTime, default=null)

)

sedes_productos = Table('sedes_productos', meta_data,
	                Column('id_sede',Integer, ForeignKey('sede.id_sede', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
                    Column('id_producto',Integer,ForeignKey('productos.id_producto', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
	                Column('stock', Integer, default=1),
                    Column('deleted_at', DateTime, default=null)

)

pedido_producto = Table('pedido_producto', meta_data,
                    Column('id_pedido', Integer, ForeignKey('pedidos.id_pedido', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
                    Column('id_producto', Integer, ForeignKey('productos.id_producto', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
                    Column('cantidad_producto', Integer, nullable=False),
                    Column('precio_unitario', DECIMAL(10,2), nullable=False),
                    Column('deleted_at', DateTime, default=null)

)

categoria_servicio = Table('categoria_servicio', meta_data,
                    Column('id_categoria_servicio', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_servicio', String(100), nullable=False),
                    Column('descripcion_servicio', String(300)),
                    Column('deleted_at', DateTime, default=null)

)

servicios = Table('servicios', meta_data,
                    Column('id_servicio', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_servicio', String(100)),
                    Column('descripcion_servicio', String(300)),
                    Column('precio_servicio', DECIMAL(10,2), nullable=False),
                    Column('id_categoria_servicio', Integer, ForeignKey('categoria_servicio.id_categoria_servicio', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
                    Column('deleted_at', DateTime, default=null)

)

clientes = Table('clientes', meta_data,
                    Column('id_cliente', Integer, primary_key=True, autoincrement=True),
                    Column('nombre_cliente', String(50), nullable=False),
                    Column('apellido_cliente', String(50)),
                    Column('telefono_cliente', String(20)),
                    Column('email_cliente', String(255)),
                    Column('cc_cliente', String(20)),
                    Column('direccion_cliente', String(100)),
                    Column('deleted_at', DateTime, default=null)

)

factura = Table('factura', meta_data,
                    Column('id_factura', Integer, primary_key=True, autoincrement=True),
                    Column('fecha_factura', DateTime,default=datetime.now()),
                    Column('total', DECIMAL(10,2), nullable=False),
                    Column('codigo_factura', String(50), nullable=False),
                    Column('id_empleado', Integer, ForeignKey('empleado.id_empleado', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
                    Column('id_cliente', Integer, ForeignKey('clientes.id_cliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
                    Column('id_sede', Integer, ForeignKey('sede.id_sede', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
                    Column('deleted_at', DateTime, default=null)

)

servicio_venta = Table('servicio_venta', meta_data,
                    Column('id_factura', Integer, ForeignKey('factura.id_factura', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
	                Column('id_servicio', Integer, ForeignKey('servicio.id_servicio', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
                    Column('cantidad', Integer, default=1),
                    Column('subtotal', DECIMAL(10,2)),
                    Column('deleted_at', DateTime, default=null)

)

producto_venta = Table('producto_venta', meta_data,
                    Column('id_factura', Integer, ForeignKey('factura.id_factura', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True),
	                Column('id_producto', Integer,ForeignKey('productos.id_producto', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
                    Column('cantidad', Integer,default=1),
	                Column('subtotal', DECIMAL(10,2)),
                    Column('deleted_at', DateTime, default=null)

)


meta_data.create_all(engine)