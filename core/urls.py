from django.urls import path, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos,
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mov-mensal/', lista_movmensalista, name='core_lista_movmensalista'),
]