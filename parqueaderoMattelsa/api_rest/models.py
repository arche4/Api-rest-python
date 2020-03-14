from django.db import models



class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombreEmp = models.CharField(max_length=50, blank=True, null=False)
    cedulaEmp = models.IntegerField()

    class Meta:
        verbose_name_plural = "EmpleadoS"
        ordering = ['id']
    def _str_(self):
        return self.id

# Create your models here.
class tipoVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_vehiculo = models.CharField(max_length=50, blank=True, null=False)
    foto= models.CharField(max_length=10000, blank=False, null=True)
    cilindraje= models.CharField(max_length=50, blank=False, null=True)
    placa = models.CharField(max_length=10, blank=False, null=True)
    modelo = models.IntegerField()
    numPuertas = models.IntegerField()
    tiempos = models.CharField(max_length=3, blank=False, null=True)
    Empleado_id = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "tipoVehiculos"
        ordering = ['id']
    def _str_(self):
        return '{}:{}'.format(self.Empleado_id.id,self.id)


class Parqueadero(models.Model):
    id = models.AutoField(primary_key=True)
    celda = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    cedulaEmp = models.IntegerField()
    tipo_vehiculo_id = models.ForeignKey(tipoVehiculo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Parqueaderos"
        ordering = ['id']
    def _str_(self):
        return '{}:{}'.format(self.tipo_vehiculo_id.id,self.id)