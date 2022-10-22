from django.db import models
from accessAplication.models import Profile
# Create your models here.

class Seccion(models.Model):
    seccionName =models.CharField(max_length=150)
    profile =models.ManyToManyField(Profile,through="EquiposRonda")
    
    def __str__(self):
        return self.seccionName

    
class EquiposRonda(models.Model):
    scouters = models.ForeignKey(Profile, on_delete=models.CASCADE)
    seccionName = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombreSeccion = models.CharField(max_length=100,null=True, blank=True)
    rondaSolar = models.IntegerField()
    def __str__(self):
        return self.seccionName.seccionName + '----'+ self.scouters.user.username+'---' +str(self.rondaSolar)





