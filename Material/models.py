
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from cloudinary.models import CloudinaryField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from sqlalchemy import null, true
from Asociados.models import Seccion
# Create your models here.
def uploadFileName(instance,filename):
    extension=filename.split('.')[1]
    fileNameTransform=str(instance.material).split('-')[0] 
    
    print(instance.material, fileNameTransform,extension)
    filePath = 'Materiales/'+fileNameTransform+'.'+extension
    filePath = 'Materiales/'+fileNameTransform
    print(filePath)
    return filePath

def uploadCloudinaryFileName(instance):
    print()
    fileNameCloudinary=str(instance.material).split('-')[0] 
    filePath = 'Materiales/'+fileNameCloudinary
    print(filePath)
    return filePath


usersChoices = [x for x in User.objects.all().values_list('username',flat=True)]

index=0
userChoicesList = []
for user in usersChoices:
    #print(index, user)
    tuplaChoice= (user,user)
    userChoicesList.append(tuplaChoice)
    index+=1
userChoicesTuple = tuple(userChoicesList)
print(userChoicesTuple)

#print(usersChoices)
#print([x for x in USUARIOS_CHOICES.values_list('User', flat=True).distinct()])
class Material(models.Model):
    NUEVO = "Nuevo"
    DESPERFECTOS_MENORES = "Desperfectos menores"
    DESPERFECTOS_MODERADOS = "Desperfectos moderados"
    DESPERFECTOS_GRAVES = "Desperfectos graves"
    ESTADO_MATERIAL = (
       ("Nuevo","Nuevo"),#('Material en perfecto estado de nuevo')
       ("Desperfectos menores",'Desperfectos menores'),# ('Pequeños Recambios que no afecta a funcionalidad')),
       ("Desperfectos moderados",'Desperfectos moderados'), #('Recambios que afectan a funcionalidad de forma leve')),
       ("Desperfectos graves",'Desperfectos graves'), #('Recambios que requieren atención inmediata')),
    )
    
    TIENDAS = "Tiendas"#1
    RECAMBIOS_TIENDAS = "Recambios Tiendas"#2
    CAMPISMO = "Campismo"#3
    HERRAMIENTAS = "Herramientas"#4
    PINTURAS = "Pinturas"#5
    ELECTRICIDAD="Electricidad"#6
    FONTANERIA="Fontanería"#7
    MESAS_BANCOS="Mesas y Bancos"#8
    INFRAESTRUCTURA_ACAMPADAS="Infraestructura Acampadas"#9
    OTROS_CAMPISMO="Otros Campismo"#39
    
    COCINA="Cocina"#40
    HORNILLOS_ROSCOS="Hornillos y Roscos"#41
    BOMBONAS_CARTUCHOS="Bombonas y Cartuchos"#42
    OTROS_COCINA="Otros Cocina"#49    

    DIDÁCTICO="Didáctico"#50
    OTROS_DIDACTICO="Otros Didáctico"#51
    
    RECAMBIOS_CAMPISMO="Recambios campismo"#90
    RECAMBIOS_ELECTRICIDAD="Recambios electricidad"#91
    RECAMBIOS_FONTANERIA="Recambios fontanería"#92
    RECAMBIOS_COCINA="Recambios cocina"#94
    

    
    TIPO_MATERIAL = (
        ("TIENDAS",'Tiendas'),
        ("Recambios tiendas",'Recambios tiendas'),
        (CAMPISMO,'Campismo'),
        (HERRAMIENTAS,'Herramientas'), 
        (PINTURAS,'Pinturas'), 
        (ELECTRICIDAD,'Electricidad'),
        (FONTANERIA,'Fontanería'),
        (MESAS_BANCOS,'Mesas y bancos'),
        (INFRAESTRUCTURA_ACAMPADAS,'Infraestructura'),
        (OTROS_CAMPISMO,'Otros campismo'),
        (COCINA,'Cocina'),
        (HORNILLOS_ROSCOS,'Hornillos y roscos'), 
        (BOMBONAS_CARTUCHOS,'Bombonas y cartuchos'), 
        (OTROS_COCINA,'Otros cocina'),
        (DIDÁCTICO,'Didáctico'),
        (OTROS_DIDACTICO,'Otros didáctico'),
        
        (RECAMBIOS_CAMPISMO,'Recambios campismo'),
        (RECAMBIOS_ELECTRICIDAD,'Recambios electricidad'),
        (RECAMBIOS_FONTANERIA,'Recambios fontanería'),
        (RECAMBIOS_COCINA,'Recambios cocina'),
       
    )
    
    
    material = models.CharField(max_length=200, null=True)
    seccion =models.ManyToManyField(Seccion,through="AsignacionMaterial")
    
    materialDescription = models.TextField(max_length=3000,null=True)
    created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    #tipoMaterial =models.CharField(choices=TIPO_MATERIAL,max_length=50,null=True, blank=True)
    #estado=models.CharField(choices=ESTADO_MATERIAL,max_length=50,null=True, default='Nuevo')
    fecha_compra=models.DateField(null=True, blank=True)
    factura = models.FileField(upload_to=uploadFileName,null=True, blank=True)
    alarma = models.BooleanField(default=False)
    #user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #User = models.CharField(choices=userChoicesTuple,max_length=50,null=True, blank=True,)
    User = models.CharField(max_length=60, null=True, blank=True)
    
    fotografia = ProcessedImageField(upload_to=uploadFileName,
                                      #processors=[ResizeToFill(600, 400)],
                                      format='JPEG',
                                      options={'quality': 60}, null=True, blank=True)

    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return  'Material: '+self.material +'  - Alta: '+ str(self.created)+'  - ID: '+ str(self.id)


class PhotoMaterial(models.Model):
    photoName = models.CharField(max_length=200, null=True, blank=True)
    #photo  = models.ImageField(upload_to="Actividades/",null=True)
    photo  = CloudinaryField(resource_type='image', folder = "media/Materiales/", transformation ={'quality':'50'},
                             use_filename=False,null=True, blank=True,public_id=uploadCloudinaryFileName
                            )
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.photoName+' - '+self.material.material
    

class RevisionMaterial(models.Model):
    
    PASA_REVISION = "pasa revision"
    DESPERFECTOS_MENORES = "Desperfectos menores"
    NECESITA_LIMPIEZA = "Necesita limpieza"
    NECESITA_REPARACION = "Necesita reparacion"
    
    RESULTADO_REVISION = (
       (PASA_REVISION,'Revisión conforme'),#('Material en perfecto estado de nuevo')
       (DESPERFECTOS_MENORES,'Desperfectos menores, reparaciones no urgentes'),# ('Pequeños Recambios que no afecta a funcionalidad')),
       (NECESITA_LIMPIEZA,'Necesita limpieza'), #('')),
       (NECESITA_REPARACION,'Necesita reparación'), #('')),
    )
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    fechaRevision = models.DateTimeField(null=True, blank=True)
    #responsableRevision = models.PositiveSmallIntegerField(choices=userChoicesTuple,null=True, blank=True)
    responsableRevision = models.CharField(max_length=60, null=True, blank=True)
    
    estadoMastiles = models.CharField(max_length=200,null=True, blank=True)
    estadoCubeta = models.CharField(max_length=200,null=True, blank=True)
    estadoDobleTecho = models.CharField(max_length=200,null=True, blank=True)
    estadoEnganches = models.CharField(max_length=200,null=True, blank=True)
    estadoBolsas = models.CharField(max_length=200,null=True, blank=True)
    numPiquetasUltraForte = models.PositiveSmallIntegerField(null=True, blank=True)
    numPiquetasForte = models.PositiveSmallIntegerField(null=True, blank=True)
    numPiquetasgEnerals = models.PositiveSmallIntegerField(null=True, blank=True)
    seGuardaSucia = models.BooleanField(default=False)
    descripcionRevision = models.TextField(null=True, blank=True)
    #resultadoRevision = models.CharField(choices=RESULTADO_REVISION,max_length=50,null=True, blank=True)
    
    desperfectosReparadosLimpios = models.BooleanField(default=False)
    fechaCierre = models.DateField(null=True, blank=True)    
    
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.material.material
    
    
class PhotoRevision(models.Model):
    revision =models.ForeignKey(RevisionMaterial, on_delete=models.CASCADE)
    photoName = models.CharField(max_length=200, null=True, blank=True)
    photo  = ProcessedImageField(upload_to="Materiales/",
                                      #processors=[ResizeToFill(600, 400)],
                                      format='JPEG',
                                      options={'quality': 60}, null=True, blank=True)
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.photoName


class AsignacionMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    seccionName = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    fechaAsignacion = models.DateField(max_length=100,null=True, blank=True)
    rondaSolar = models.IntegerField()
    def __str__(self):
        return self.seccionName.seccionName + '----'+ self.material.material+'---' +str(self.rondaSolar)

