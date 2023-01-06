from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=100)
    website= models.URLField(max_length=100)
    foundation= models.PositiveIntegerField()

    def __str__(self):
        return self.name
