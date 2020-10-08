from django.contrib import admin
from .models import Usuario, Transporte, TipoUsuario, Subasta, SolicitudVentaLocal, SolicitudTransporte, Seguro, PublicacionVenta, Producto, ProcesoVenta, Pais, Moneda, Inventario, FormatoProducto, EstadoProducto, DetalleVenta, Cuenta, Contrato, Ciudad, CalidadProducto, BrUsuariosProcesoDeVenta, BrProductosProcesoDeVenta

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Transporte)
admin.site.register(TipoUsuario)
admin.site.register(Subasta)
admin.site.register(SolicitudVentaLocal)
admin.site.register(SolicitudTransporte)
admin.site.register(Seguro)
admin.site.register(PublicacionVenta)
admin.site.register(Producto)
admin.site.register(ProcesoVenta)
admin.site.register(Pais)
admin.site.register(Moneda)
admin.site.register(Inventario)
admin.site.register(FormatoProducto)
admin.site.register(EstadoProducto)
admin.site.register(DetalleVenta)
admin.site.register(Cuenta)
admin.site.register(Contrato)
admin.site.register(Ciudad)
admin.site.register(CalidadProducto)
admin.site.register(BrUsuariosProcesoDeVenta)
admin.site.register(BrProductosProcesoDeVenta)
