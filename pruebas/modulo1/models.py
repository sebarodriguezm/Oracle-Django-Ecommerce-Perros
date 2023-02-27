from django.db import models
from django.contrib.auth.models import User

    
class Categoria(models.Model):   

    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500) 
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True) 
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nombre        
    
class Raza(models.Model):   
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)
    peso = models.IntegerField()
    cuidados = models.BooleanField(default=True)
    imagen = models.ImageField()
    precio = models.IntegerField()
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
            return self.nombre   
        
    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'     

    @property 
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
          
class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200 )
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
                
class Marca(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField()
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return self.nombre     
        
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=200)
    peso = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    oferta = models.BooleanField(default=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField()
    precio = models.IntegerField()
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return self.nombre 
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    