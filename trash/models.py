from django.db import models

class Trash(models.Model):
   organic = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
   inOrganic = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
   
class TrashType(models.Model):
   name = models.CharField(max_length=50)