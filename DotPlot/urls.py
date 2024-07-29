
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patientList, name='patient_list'),
]





