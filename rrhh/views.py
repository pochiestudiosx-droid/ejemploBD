from django.shortcuts import render
from rrhh.models import Empleado
# Create your views here.
def index(request):
    return render(request, 'consultas.html')

def ejecutar(request,id):
    empleados = Empleado.objects.all()
    cantidad = Empleado.objects.all().count()
    data = {'empleados': empleados, 'cantidad':cantidad}
    return render(request, 'listadoEmpleados.html', data)