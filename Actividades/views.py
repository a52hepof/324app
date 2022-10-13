import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pandas import isnull
from sqlalchemy import null
from .forms import ActividadesForm
from Actividades.templates import *
from .models import Activity, User
 

# Create your views here.
def helloworld(request):
    return HttpResponse('<h1>hello world</h1>')

def actividadeMain(request):
    #actividades = Activity.objects.all()
    #actividades = Activity.objects.filter(user=request.user,files__isnull=True)
    actividades = Activity.objects.filter(user=request.user,fecha_evaluacion__isnull=True)
    for  actividad in actividades:
        print(actividad)
    Author = 'Milano'
    grupo = 'Grupo Scout Baden Powell'
    return render(request, 'actividadesMain.html', 
        {
        'user': request.user,
        'autor': Author , 
        'actividades':actividades
        
        }
    )
    
def actividadCreada(request, idActividad):
     
    Author = 'Milano'
    grupo = 'Grupo Scout Baden Powell'
    return render(request, 'actividadCreada.html', 
        {
        'autor': Author , 
        'idActividad': idActividad,
        }
    )
    
def crearActividad(request):
    username = request.user.id
    #print(type(username))
    Author = 'Milano'
    grupo = 'Grupo Scout Baden Powell'
    print(request.user)
    usuario = request.user
    UserObject = User.objects.all()
    print(UserObject, request.user, username)
    
    if type(username) == 'NoneType' or username == None:
        print('Regístrese')
        return redirect('signin')
       

    
    if request.method == 'GET':
        
        return render(request, 'crearActividad.html', 
            {
            'form': ActividadesForm,
            'autor': Author , 
            }
        )
        
    else:
        try:
            formulario = ActividadesForm(request.POST)
            print(request.user)
            #if formulario.is_valid():
            nuevaActividad = formulario.save(commit=True)
            #nuevaActividad.user = request.user
            print(nuevaActividad)
            nuevaActividad.save()
            idActividad=nuevaActividad.id 
            
            return redirect('actividadcreada', idActividad)
        except:
            print('Algo ha ido mal')
            
            return render(request, 'crearActividad.html', 
                {
                'form': ActividadesForm,
                'autor': Author , 
                'error':'Proporciona los datos correctos para dar de alta la actividad'
                }
            )
            