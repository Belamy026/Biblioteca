from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=True)
    apellido = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=True)
    apellido = models.CharField(max_length=100, blank=False, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.cliente} - {self.libro}'

class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    fecha_multa = models.DateField()
    importe = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.prestamo} - {self.importe}'