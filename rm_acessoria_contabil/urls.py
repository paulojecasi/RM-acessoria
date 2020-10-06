from django.urls import path
from .views import acessoriaContabil

urlpatterns = [
    path('acessoria/',acessoriaContabil),
]
