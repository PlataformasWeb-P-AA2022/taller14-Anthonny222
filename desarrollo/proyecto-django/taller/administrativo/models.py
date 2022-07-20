from django.db import models


class Propietario(models.Model):
    opciones_nacionalidad = (
        ('ecuatoriana', 'Ecuatoriana'),
        ('peruana', 'Peruana'),
        ('colombiana', 'Colombiana'),
    )
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30, unique=True)
    nacionalidad = models.CharField(
        max_length=30, choices=opciones_nacionalidad)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                                self.apellido,
                                self.edad,
                                self.nacionalidad)


class Departamento(models.Model):
    costo = models.CharField(max_length=100)
    cuartos = models.CharField(max_length=100)
    banio = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
                                    related_name="Departamentos")

    def __str__(self):
        return "%s %s %s %s" % (self.costo, self.cuartos, self.banio, self.valor)
