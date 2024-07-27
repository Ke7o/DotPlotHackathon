from django.shortcuts import render
from .models import Patients

def patientList (request):
    query = request.GET.get('q')

    if query:
        patients = Patients.objects.filter(patientID=query)
    
    else:
        patients = Patients.objects.all()
    
    return render(request, 'patients_list.html', {'patients': patients})