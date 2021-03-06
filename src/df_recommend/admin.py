from django.contrib import admin
from .models import TypeInfo, GoodsInfo

# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']     #admin attributes

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 100              #admin how much product per page
    list_display = ['id', 'gtitle', 'gprice', 'gunit','gclick', 'gkucun', 'gcontent', 'gtype']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
