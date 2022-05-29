from django.db import models

# Create your models here.


class Catalog(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)

    def __str__(self):
        return self.title
