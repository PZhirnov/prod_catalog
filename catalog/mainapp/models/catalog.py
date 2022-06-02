from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.


class Catalog(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.title
