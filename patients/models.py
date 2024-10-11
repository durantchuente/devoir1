from django.db import models

class Patient(models.Model):
    nom_complet = models.CharField(max_length=255)
    date_naissance = models.DateField()
    SEXE_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme'),
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    GROUPE_SANGUIN_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    groupe_sanguin = models.CharField(max_length=3, choices=GROUPE_SANGUIN_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    historique_medical = models.TextField(blank=True, null=True)
    consentement = models.BooleanField(default=False)
    def __str__(self):
        return self.nom_complet
