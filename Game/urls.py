from django.urls import path 
from .views import *

urlpatterns = [
	path('', index, name = "index"),
	path('index/<int:valor_inicial>', home, name = "home")
]