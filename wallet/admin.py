from django.contrib import admin
from .models import  article,ann
# Register your models here.



class articleAdmin(admin.ModelAdmin):
        fields = ('title','introduce','urlDetail','thumbnailImage',)
admin.site.register(article,articleAdmin)


# @admin.register(ann)
class annAdmin(admin.ModelAdmin):
         fields = ('title',)
admin.site.register(ann,annAdmin)
