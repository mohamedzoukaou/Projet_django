from django.db import models
from django.utils import timezone
from django.conf import settings

class Employer(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    date_embauche = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nom

class Departement(models.Model):
    nom_departement = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_departement



