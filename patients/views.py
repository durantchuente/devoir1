from django.shortcuts import render, redirect
from patients.forms import PatientForm
from patients.models import Patient

def patient_list(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        else:
            print(form.errors)  # Affichez les erreurs dans la console pour déboguer
    else:
        form = PatientForm()

    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'form': form, 'patients': patients})
