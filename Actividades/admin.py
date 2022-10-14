from django.contrib import admin
from Actividades.models import Activity, PhotoActivity
# Register your models here.

class PhotoActivityAdmin(admin.StackedInline):
    model = PhotoActivity
    extra = 0

class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    #exclude = ('realizada',)
    inlines = [PhotoActivityAdmin]




admin.site.register(Activity, ActivityAdmin)
#admin.site.register(PhotoActivity)
