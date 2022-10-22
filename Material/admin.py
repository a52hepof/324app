

from django.contrib import admin


#from Material.models import Material, PhotoMaterial, RevisionMaterial, PhotoRevision, AsignacionMaterial
from Material.models import Material
from django.utils.html import format_html
# Register your models here.
from django.conf import settings
'''
class PhotoMaterialAdmin(admin.StackedInline):
    model = PhotoMaterial
    extra = 0

class RevisionMaterialAdmin(admin.StackedInline):
    model = RevisionMaterial
    extra = 0
    

class MaterialAdmin(admin.ModelAdmin):
    search_fields = ("material", "materialDescription")
    readonly_fields = ('created',)
    #list_display = ("material", "materialDescription","tipoMaterial","foto")
    list_display = ("material", "materialDescription","foto")
    #list_filter = ("tipoMaterial", )
    #exclude = ('realizada',)
    inlines = [PhotoMaterialAdmin,RevisionMaterialAdmin]
    def foto(self, obj):
        #print(obj.files_thumbnail)
        #print(settings.CLOUDINARY_PATH)
        thumbail = settings.CLOUDINARY_PATH + str(obj.fotografia)
        if obj.fotografia:
            return format_html('<a title="Los Tejos" href={}> <img src={} width="100" height="100" /></a>',thumbail,thumbail)


# Register your models here.
admin.site.register(Material,MaterialAdmin )
admin.site.register(AsignacionMaterial)
'''
admin.site.register(Material)