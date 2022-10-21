from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from cloudinary.models import CloudinaryField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from sqlalchemy import null, true

# Create your models here.


class Material(models.Model):
    material = models.CharField(max_length=200, null=True)
    materialDescription = models.TextField(max_length=3000,null=True)
    created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    tipoMaterial =models.CharField(max_length=100,null=True)
    fecha_compra=models.DateTimeField(null=True, blank=True)
    factura = models.FileField(upload_to="Materiales/",null=True, blank=True)
    user = models.CharField(max_length=100,null=True)
    fotografia = ProcessedImageField(upload_to="Materiales/",
                                      #processors=[ResizeToFill(600, 400)],
                                      format='JPEG',
                                      options={'quality': 60}, null=True, blank=True)

    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.material +' - '+ self.materialDescription


class PhotoMaterial(models.Model):
    photoName = models.CharField(max_length=200, null=True, blank=True)
    #photo  = models.ImageField(upload_to="Actividades/",null=True)
    photo  = CloudinaryField(resource_type='image', folder = "media/Materiales/", transformation ={'quality':'50'},
                             use_filename=True,null=True
                            )
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.photoName+' - '+self.material.material
    

class RevisionMaterial(models.Model):
    material =models.ForeignKey(Material, on_delete=models.CASCADE)
    fechaRevision = models.DateTimeField(null=True, blank=True)
    descripcionRevision = models.TextField(null=True, blank=True)
    def __str__(self):
        #return '%s - %s' %(self.titulo, self.description)
        return self.material
    
    
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
    