from django.shortcuts import render, redirect
from .forms import *
import random

# Create your views here.
def index(request):


	if request.method == "GET":
		return render(request, 'home.html')

	else:
		valor_inicial = random.randint(1,100)
		valor_inicial = valor_inicial * 1231231243232131
		return redirect(f"index/{valor_inicial}")

def home(request, valor_inicial):

	valor_inicial = valor_inicial / 1231231243232131
	print(valor_inicial)
	valor = 0

	if request.method == "GET":
		return render(request, 'index.html', {"Game":Game, "valor":valor})
	else:
		numero = request.POST["numero"]
		numero = int(numero)

		if numero < 0 or numero > 100:
			valor = 3
			return render(request, 'index.html', {"Game":Game, "valor":valor})
		elif numero < valor_inicial:
			valor = 1
			return render(request, 'index.html', {"Game":Game, "valor":valor})
		elif numero > valor_inicial:
			valor = 2
			return render(request, 'index.html', {"Game":Game, "valor":valor})
		elif numero == valor_inicial:
			return render(request, 'felicitaciones.html', {"valor":numero})
