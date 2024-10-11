from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        # model = Patient
        # fields = ['nom_complet', 'date_naissance', 'sexe', 'telephone', 'email', 'adresse', 'historique_medical', 'groupe_sanguin']
        # exclude = ['date_enregistrement']
        model = Patient
        fields = '__all__'
