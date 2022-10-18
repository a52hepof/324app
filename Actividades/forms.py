from django.forms import ModelForm
from django import forms
from .models import Activity, PhotoActivity

class ActividadesForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['titulo', 'description','num_responsables','num_participantes'
                  #,'tipo_actividad','user','realizada']
                  ,'tipo_actividad','files', 'files_thumbnail' ]
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'num_responsables': forms.TextInput(attrs={'class':'form-control'}),
            'num_participantes': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_actividad': forms.TextInput(attrs={'class':'form-control'}),

            
        }
        #fields = '__all__'
        #exclude = []