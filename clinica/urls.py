from django.urls import path,include
from .views import PacienteView,ConsultaView,EspecialistaView,PcienteFumador,PacienteViejo
from clinica import views


urlpatterns = [
    path('hospital/paciente',PacienteView.as_view(),name='paciente'),
    path('hospital/consulta',ConsultaView.as_view(),name='consulta'),
    path('hospital/especialista',EspecialistaView.as_view(),name='especialista'),
    path('hopital/consulta/<str:pk>',ConsultaView.as_view(),name='cambio'),
    path('hospital/pacientefumador',PcienteFumador.as_view()),
    path('hospital/PacienteViejo',PacienteViejo.as_view())
]