from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/medicamentos', medicamentos, name='medicamentos'),
    path('api/fichas', ficha ,name='ficha'),
    path('api/prescripcion', prescripcion ,name='prescripcion'),
    path('api/gestMed/<id_medicamento>', gestMed, name='gestMed'),
    path('api/gestFicha/<id_ficha>', gestFicha, name='gestFicha'),
    path('api/gestPrescripcion/<id_prescripcion>', gestPrescripcion, name='gestPrescripcion'),
    path('', ApiRoot.as_view(), name='api_root'),
]
