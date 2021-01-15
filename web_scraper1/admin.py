from django.contrib import admin
from .models import Tags
# Register your models here.
@admin.register(Tags)
class  UserAdmin(admin.ModelAdmin):
    list_display=('id','tag','tag1','tag2','tag3','tag4','tag5','tag6','tag7','tag8','tag9','tag10')
