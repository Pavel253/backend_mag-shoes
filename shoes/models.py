from django.db import models

class Shoes(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    price = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    image = models.ImageField(null=True, blank=True)

    fonImage1 = models.ImageField(null=True, blank=True)
    fonImage2 = models.ImageField(null=True, blank=True)
    fonImage3 = models.ImageField(null=True, blank=True)
    fonImage4 = models.ImageField(null=True, blank=True)
    fonImage5 = models.ImageField(null=True, blank=True)

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, null=True)
    color = models.ForeignKey('Color', on_delete=models.PROTECT, null=True)
    color1 = models.ForeignKey('Color1', on_delete=models.PROTECT, null=True)
    color2 = models.ForeignKey('Color2', on_delete=models.PROTECT, null=True)
    color3 = models.ForeignKey('Color3', on_delete=models.PROTECT, null=True)
    size = models.ForeignKey('Size', on_delete=models.PROTECT, null=True)
    quantity = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    

class Color1(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    

class Color2(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    

class Color3(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
