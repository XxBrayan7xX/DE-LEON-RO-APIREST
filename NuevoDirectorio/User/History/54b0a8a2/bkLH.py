from django.shortcuts import render
from persona.models import Persona
# Create your views here.
def index(request):
	return render(request,'bienvenido.html')

def indexPersona(request):
	personas = Persona.objects.order_by('id')
	print(personas[0].nombre)
	return render(request,'indexPerson.html', {personas:personas})