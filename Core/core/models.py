from django.db import models


class Categorias(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="Id de Categoria")
    CategoriaDejuego = models.CharField(max_length=50,verbose_name="Categoria del juego")
    

    def __str__(self):
        return self.CategoriaDejuego


class Pag1juegos(models.Model):
    Codigo = models.CharField(max_length=6, primary_key=True, verbose_name="CodigoJuego")
    NombreDelJuego = models.CharField(max_length=50,verbose_name="NombreDeljuego")
    CompañiaCreadora = models.CharField(max_length=50,verbose_name="CompañiaCreadora")
    Plataforma = models.CharField(max_length=50,null= True,blank=True,verbose_name="Plataforma")
    Descripcion = models.CharField(max_length=200,null= True,blank=True,verbose_name="Descripcion")
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Caratula=models.ImageField(upload_to="Caratulas",null=True)
    def __str__(self):
        return self.NombreDelJuego

class MundoAbierto(models.Model):
    Codigo = models.CharField(max_length=6, primary_key=True, verbose_name="CodigoJuego")
    NombreDelJuego = models.CharField(max_length=50,verbose_name="NombreDeljuego")
    CompañiaCreadora = models.CharField(max_length=50,verbose_name="CompañiaCreadora")
    Plataforma = models.CharField(max_length=50,null= True,blank=True,verbose_name="Plataforma")
    Descripcion = models.CharField(max_length=200,null= True,blank=True,verbose_name="Descripcion")
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Caratula=models.ImageField(upload_to="Caratulas",null=True)
    def __str__(self):
        return self.NombreDelJuego

class Rol (models.Model):
    Codigo = models.CharField(max_length=6, primary_key=True, verbose_name="CodigoJuego")
    NombreDelJuego = models.CharField(max_length=50,verbose_name="NombreDeljuego")
    CompañiaCreadora = models.CharField(max_length=50,verbose_name="CompañiaCreadora")
    Plataforma = models.CharField(max_length=50,null= True,blank=True,verbose_name="Plataforma")
    Descripcion = models.CharField(max_length=200,null= True,blank=True,verbose_name="Descripcion")
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Caratula=models.ImageField(upload_to="Caratulas",null=True)
    def __str__(self):
        return self.NombreDelJuego 

class Aventura(models.Model):
    Codigo = models.CharField(max_length=6, primary_key=True, verbose_name="CodigoJuego")
    NombreDelJuego = models.CharField(max_length=50,verbose_name="NombreDeljuego")
    CompañiaCreadora = models.CharField(max_length=50,verbose_name="CompañiaCreadora")
    Plataforma = models.CharField(max_length=50,null= True,blank=True,verbose_name="Plataforma")
    Descripcion = models.CharField(max_length=200,null= True,blank=True,verbose_name="Descripcion")
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Caratula=models.ImageField(upload_to="Caratulas",null=True)
    def __str__(self):
        return self.NombreDelJuego

class Lucha(models.Model):
    Codigo = models.CharField(max_length=6, primary_key=True, verbose_name="CodigoJuego")
    NombreDelJuego = models.CharField(max_length=50,verbose_name="NombreDeljuego")
    CompañiaCreadora = models.CharField(max_length=50,verbose_name="CompañiaCreadora")
    Plataforma = models.CharField(max_length=50,null= True,blank=True,verbose_name="Plataforma")
    Descripcion = models.CharField(max_length=200,null= True,blank=True,verbose_name="Descripcion")
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Caratula=models.ImageField(upload_to="Caratulas",null=True)
    def __str__(self):
        return self.NombreDelJuego                                      