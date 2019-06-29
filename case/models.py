from django.db import models

# Create your models here.
class Case(models.Model):
    casetitle = models.CharField(max_length=50, unique=True)
    casetitle_long = models.CharField(max_length=250, unique=True)
    arbitration_rules = models.CharField(max_length=50,null=True, blank=True)
    decisions_rendered = models.CharField(max_length=50,null=True, blank=True)
    link = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.casetitle