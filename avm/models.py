from django.db import models

class Turno(models.Model):
   
    fecha = models.DateField()
    hora = models.TimeField()


    # campos que provienen de la relacion con otras tablas
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    mecanico = models.ForeignKey('Mecanico', on_delete=models.CASCADE)
    

    # este def nos permite mostrar el nombre del turno en el admin
    def __str__(self):
        return f'{self.fecha} - {self.hora}'


class Vehiculo(models.Model):

    anio = models.IntegerField()

    tipo_vehiculo = models.CharField(max_length=50)

    marca = models.CharField(max_length=50)

    modelo = models.CharField(max_length=50)

    matricula = models.CharField(max_length=50)
    
    utilidad = models.CharField(max_length=50)

    nro_chasis = models.CharField(max_length=50)
   

    # este def nos permite mostrar el nombre del vehiculo en el admin
    def __str__(self):
        return f'{self.marca} - {self.modelo}'


class Mecanico(models.Model): 
    
    # suponemos que el mecanico tiene un estado activo o inactivo
    estado = models.BooleanField()
    
    especialidad = models.CharField(max_length=50)

    nombre = models.CharField(max_length=50)
  
    certificacion = models.CharField(max_length=50)

    anios_experiencia = models.IntegerField()
    
    # este def nos permite mostrar el nombre del mecanico en el admin
    def __str__(self):
        return f'Mecanico especializado en: {self.especialidad}'
