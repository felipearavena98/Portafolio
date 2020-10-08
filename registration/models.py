from django.db import models

# Create your models here.


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    detalle_pais = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    detalle_ciudad = models.CharField(max_length=150)
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'ciudad'

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

