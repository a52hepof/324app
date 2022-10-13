from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from sqlalchemy import ForeignKey, false, null
from cloudinary.models import CloudinaryField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()



class Activity(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=3000,null=True)
    created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    num_responsables = models.IntegerField(default=1, verbose_name="NResponsables")
    num_participantes = models.IntegerField(default=2, verbose_name="NParticipantes")
    tipo_actividad =models.CharField(max_length=100,null=True)
    fecha_evaluacion = models.DateField(null=True, blank=True)
    
    #images = models.ImageField(upload_to="Actividades/",default="")
    #images  = CloudinaryField(resource_type='image', folder = "media/Actividades/", transformation ={'quality':'50'},use_filename=True,null=True)
    #files  = CloudinaryField(resource_type='raw', folder = "media/Actividades/", transformation ={'quality':'50'},use_filename=True,null=True)                        
    files = models.FileField(upload_to="Actividades/",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    files_thumbnail = ProcessedImageField(upload_to="Actividades/",
                                      processors=[ResizeToFill(600, 400)],
                                      format='JPEG',
                                      options={'quality': 60}, null=True, blank=True)

    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.titulo +' - '+ self.description


class PhotoActivity(models.Model):
    photoName = models.CharField(max_length=200,null=True)
    #photo  = models.ImageField(upload_to="Actividades/",null=True)
    photo  = CloudinaryField(resource_type='image', folder = "media/Actividades/", transformation ={'quality':'50'},
                             use_filename=True,null=True
                            )
    
    
    activity =models.ForeignKey(Activity, on_delete=models.CASCADE)
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.photoName +' - '
        