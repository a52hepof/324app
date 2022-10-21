from django.contrib import admin
from Actividades.models import Activity, PhotoActivity
from django.utils.html import format_html
# Register your models here.
from django.conf import settings

class PhotoActivityAdmin(admin.StackedInline):
    model = PhotoActivity
    extra = 0
    

class ActivityAdmin(admin.ModelAdmin):
    search_fields = ("titulo", "description")
    readonly_fields = ('created',)
    list_display = ("titulo", "description","tipo_actividad","foto")
    list_filter = ("tipo_actividad", )
    #exclude = ('realizada',)
    inlines = [PhotoActivityAdmin]
    def foto(self, obj):
        #print(obj.files_thumbnail)
        #print(settings.CLOUDINARY_PATH)
        thumbail = settings.CLOUDINARY_PATH + str(obj.files_thumbnail)
        if obj.files_thumbnail:
            return format_html('<a title="Los Tejos" href={}> <img src={} width="100" height="100" /></a>',thumbail,thumbail)
        

'''
@admin.register(ActivityAdmin)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("titulo", "description","tipo_actividad")
    list_filter = ("tipo_actividad", )
'''    
    
    
admin.site.register(Activity, ActivityAdmin)
#admin.site.register(PhotoActivity)
