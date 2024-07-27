from django.shortcuts import render
from .models import Patients

def patientList(request):
    query = request.GET.get('search-patient-id')
    patient = None

    if query:
        try:
            patient = Patients.objects.get(patientID=query)
        except Patients.DoesNotExist:
            patient = None

    return render(request, 'patients_list.html', {'patient': patient})
