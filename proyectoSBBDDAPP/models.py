from django.db import models

# Create your models here.

#Cada clase es una tabla de la BD
#Si no se especifica la primary key, se crea automaticamente

class domicilio(models.Model):
    codigo_domicilio=models.BigAutoField(primary_key=True)
    calle=models.CharField(max_length=50)
    colonia=models.CharField(max_length=50)
    numero=models.CharField(max_length=5)
    municipio=models.CharField(max_length=50)
    #Para que el el sitio de admin muestre la calle y no un objeto
    def __str__(self):
        return f'[{self.codigo_domicilio}] {self.calle}, {self.colonia}'

class usuario(models.Model):
    codigo_cliente=models.BigAutoField(primary_key=True)
    codigo_domicilio=models.OneToOneField(domicilio, 
                                          on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    def __str__(self):
        return f'[{self.codigo_cliente}] {self.nombre}'

class tecnico(models.Model):
    codigo_tecnico=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return f'[{self.codigo_tecnico}] {self.nombre}'

class reporte(models.Model):
    folio=models.BigAutoField(primary_key=True)
    motivo_reporte=models.IntegerField(default=1)
    estado_reporte=models.BooleanField(default=False)
    codigo_cliente=models.ForeignKey(usuario, on_delete=models.CASCADE, default=0)
    codigo_tecnico=models.ForeignKey(tecnico, on_delete=models.CASCADE, default=0)

class registros(models.Model):
    id_consulta = models.BigAutoField(primary_key=True)
    folio = folio=models.OneToOneField(reporte, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    