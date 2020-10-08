from django.db import models


class BrProductosProcesoDeVenta(models.Model):
    id_productos_proceso = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_pventa = models.ForeignKey('ProcesoVenta', models.DO_NOTHING, db_column='id_pventa')

    class Meta:
        managed = False
        db_table = 'br_productos_proceso_de_venta'


class BrUsuariosProcesoDeVenta(models.Model):
    id_br_usuarios_proceso = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_cliente')
    id_pventa = models.ForeignKey('ProcesoVenta', models.DO_NOTHING, db_column='id_pventa')

    class Meta:
        managed = False
        db_table = 'br_usuarios_proceso_de_venta'


class CalidadProducto(models.Model):
    id_calidad = models.AutoField(primary_key=True)
    detalle_calidad = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'calidad_producto'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    detalle_ciudad = models.CharField(max_length=150)
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    detalle_contrato = models.CharField(max_length=150)
    fecha_inicio = models.CharField(max_length=20)
    fecha_actualizacion = models.CharField(max_length=20)
    fecha_termino = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'contrato'


class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    monto = models.BigIntegerField()
    id_cliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'cuenta'


class DetalleVenta(models.Model):
    id_dventa = models.AutoField(primary_key=True)
    descripcion_dventa = models.CharField(max_length=150)
    iva = models.DecimalField(max_digits=2, decimal_places=1)
    monto = models.BigIntegerField()
    monto_total = models.BigIntegerField()
    cuotas = models.BigIntegerField()
    monto_envio = models.BigIntegerField(blank=True, null=True)
    monto_aduana = models.BigIntegerField(blank=True, null=True)
    pago_servicios = models.BigIntegerField(blank=True, null=True)
    comision_empresa = models.BigIntegerField(blank=True, null=True)
    id_moneda = models.ForeignKey('Moneda', models.DO_NOTHING, db_column='id_moneda')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class EstadoProducto(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion_estado = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'estado_producto'


class FormatoProducto(models.Model):
    id_formato = models.AutoField(primary_key=True)
    nombre_formato = models.CharField(max_length=150)
    descripcion_formato = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'formato_producto'


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class Moneda(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    detalle_moneda = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'moneda'


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    detalle_pais = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class ProcesoVenta(models.Model):
    id_pventa = models.AutoField(primary_key=True)
    cantidad = models.BigIntegerField()
    tipo_venta = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    unidades_vendidas = models.CharField(max_length=150)
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato', blank=True, null=True)
    id_dventa = models.ForeignKey(DetalleVenta, models.DO_NOTHING, db_column='id_dventa', blank=True, null=True)
    id_subasta = models.ForeignKey('Subasta', models.DO_NOTHING, db_column='id_subasta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proceso_venta'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=150)
    id_estado = models.ForeignKey(EstadoProducto, models.DO_NOTHING, db_column='id_estado')
    id_calidad = models.ForeignKey(CalidadProducto, models.DO_NOTHING, db_column='id_calidad')
    id_formato = models.ForeignKey(FormatoProducto, models.DO_NOTHING, db_column='id_formato')
    id_inventario = models.ForeignKey(Inventario, models.DO_NOTHING, db_column='id_inventario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class PublicacionVenta(models.Model):
    id_producto_en_venta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio_unitario = models.BigIntegerField()
    imagen = models.BinaryField()
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'publicacion_venta'


class Seguro(models.Model):
    id_seguro = models.AutoField(primary_key=True)
    cobrado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'seguro'


class SolicitudTransporte(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    costo = models.BigIntegerField()
    id_subasta = models.ForeignKey('Subasta', models.DO_NOTHING, db_column='id_subasta')
    id_transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='id_transporte')

    class Meta:
        managed = False
        db_table = 'solicitud_transporte'


class SolicitudVentaLocal(models.Model):
    id_solicitud_venta_local = models.AutoField(primary_key=True)
    estado_solicitud = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=30)
    descripcion_producto = models.CharField(max_length=100)
    imagen = models.BinaryField()
    estado_producto = models.CharField(max_length=30)
    calidad_producto = models.CharField(max_length=30)
    formato_producto = models.CharField(max_length=30)
    id_cliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'solicitud_venta_local'


class Subasta(models.Model):
    id_subasta = models.AutoField(primary_key=True)
    plazo = models.DateField()
    solicitud_ganadora = models.BigIntegerField(blank=True, null=True)
    id_seguro = models.ForeignKey(Seguro, models.DO_NOTHING, db_column='id_seguro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subasta'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Transporte(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    tamano = models.CharField(max_length=150)
    capacidad_carga = models.CharField(max_length=150)
    refrigeracion = models.CharField(max_length=1)
    id_cliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'transporte'


class Usuario(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    usuario = models.CharField(max_length=15)
    pass_field = models.CharField(db_column='pass', max_length=15)  # Field renamed because it was a Python reserved word.
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=30)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = False
        db_table = 'usuario'
