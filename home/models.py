from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=250,unique=True)
    descripcion = models.CharField(max_length=500, blank=True,null=True)
    status = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='productos',blank=True,null=True)

    categorias = models.ManyToManyField(Categoria, null=True, blank=True) 
    marca = models.ForeignKey(Marca,on_delete= models.PROTECT)# Relación ManyToMany

    def __str__(self):
        return self.nombre