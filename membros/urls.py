<<<<<<< HEAD
from django.urls import path
from membros import views

urlpatterns = [
    path('', views.cadastro, name='home'),           # ← /  →  cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
]
=======
# core/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path("ajuda/", views.ajuda, name="ajuda"),
]
>>>>>>> bcd0b793903ead3db7abd96c652dc05a2698ce26
