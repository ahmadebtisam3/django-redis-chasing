from django.contrib import admin
from Articals.models import Artical
from django.contrib.admin.options import ModelAdmin
# Register your models here.


class ArticalAdmin(ModelAdmin):
    list_display = ["name", "text"]
    search_fields = ["name", "text"]


admin.site.register(Artical, ArticalAdmin)
