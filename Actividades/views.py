import http
from multiprocessing.sharedctypes import Value
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
import Actividades
from .forms import ActividadesForm
from Actividades.templates import *
from .models import Activity, User

from django.contrib.auth.decorators import login_required
 

# Create your views here.
def helloworld(request):
    return HttpResponse('<h1>hello world</h1>')

@login_required
def actividadListado(request):
    #actividades = Activity.objects.all()
    #actividades = Activity.objects.filter(user=request.user,files__isnull=True)
    #print(request.user)
    #actividades = Activity.objects.filter(user=request.user,fecha_evaluacion__isnull=False).order_by('-fecha_evaluacion')
    #actividades = Activity.objects.filter(user=request.user,realizada=False)
    actividades = Activity.objects.filter(user=request.user)
    #for  actividad in actividades:
    #    print(actividad)
    Author = 'Milano'
    grupo = 'Grupo Scout Baden Powell'
    return render(request, 'actividadLista.html', 
        {
        'user': request.user,
        'autor': Author , 
        'actividades':actividades
        
        }
    )
    
@login_required
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
    #print(request.user)
    usuario = request.user
    UserObject = User.objects.all()
    #print(UserObject, request.user, username)
    
    if type(username) == 'NoneType' or username == None:
        #print('Regístrese')
        return redirect('signin')
       

    
    if request.method == 'GET':
        
        return render(request, 'actividadCrear.html', 
            {
            'form': ActividadesForm,
            'autor': Author , 
            }
        )
        
    else:
        try:
            formulario = ActividadesForm(request.POST)
            #print(request.user, request.user.id, request.user.username)
            #if formulario.is_valid():
            nuevaActividad = formulario.save(commit=False)
            nuevaActividad.user = request.user
            #print(nuevaActividad)
            nuevaActividad.save()
            idActividad=nuevaActividad.id 
            
            #return redirect('actividadcreada', {'idActividad':idActividad,'actividad':nuevaActividad}) ## esto no funciona
            return redirect('actividadcreada', idActividad)
        except:
            print('Algo ha ido mal')
            
            return render(request, 'actividadCrear.html', 
                {
                'form': ActividadesForm,
                'autor': Author , 
                'error':'Proporciona los datos correctos para dar de alta la actividad',
                'actividad':nuevaActividad
                }
            )

@login_required
def actividadDetalle(request,idActividad):
    #print(idActividad)
    #actividad = Activity.objects.get(pk=idActividad)
    if  request.method == 'GET':
        actividad = get_object_or_404(Activity,pk=idActividad, user=request.user)
        form = ActividadesForm(instance=actividad)
        
        return render(request, 'actividadDetalle.html',
                    {'actividad':actividad, 'formularioActividad' : form})
    
    else:
        
        try:
            actividad = get_object_or_404(Activity,pk=idActividad,user=request.user)
            form = ActividadesForm(request.POST, instance=actividad)
            form.save()  
            return redirect('actividades')      
            #return render(request, 'actividadDetalle.html',{'actividad':actividad, 'formularioActividad' : form})
        except ValueError:
            return render (request, 'actividadDetalle.html',
                           {'actividad':actividad, 'formularioActividad' : form, 'error':"error actualizando la Actividad"}) 

@login_required       
def actividadRealizar(request,idActividad):
    actividad = get_object_or_404(Activity,pk=idActividad,user=request.user)
    #print(actividad,request.method)
    if request.method == 'POST':
        actividad.realizada = True
        print(actividad)
        actividad.save()
    return redirect('actividades')
    return render (request,'actividadRealizar.html',
                   {'idActividad':idActividad}) 
    
@login_required       
def actividadEliminar(request,idActividad):
    actividad = get_object_or_404(Activity,pk=idActividad,user=request.user)
    #print(actividad,request.method)
    if request.method == 'POST':
        actividad.delete()
    return redirect('actividades')
    return render (request,'actividadRealizar.html',
                   {'idActividad':idActividad}) 