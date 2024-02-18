from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    image = models.ImageField(null=True, blank=True)

    fonImage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title