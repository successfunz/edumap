from django.urls import path
from membros import views

urlpatterns = [
    path('', views.cadastro, name='home'),           # ← /  →  cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
]