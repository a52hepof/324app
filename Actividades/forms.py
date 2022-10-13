from django.forms import ModelForm
from .models import Activity, PhotoActivity

class ActividadesForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['titulo', 'description','num_responsables','num_participantes'
                  #,'tipo_actividad','user']
                  ,'tipo_actividad','user']
        #fields = '__all__'
        #exclude = []