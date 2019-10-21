from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Complain

class ComplainAdmin(ImportExportModelAdmin):
# class ComplainAdmin(admin.ModelAdmin):
    list_display = ('customer', 'complaintitle', 'name', 'email','pn', 'gender', 'complain', 'treated')
    list_per_page = 5
    search_fields = ('customer', 'complaintitle', 'name', 'email','pn', 'gender', 'complain', 'treated')
    list_filter = ('customer', 'complaintitle', 'name', 'email','pn', 'gender', 'complain', 'treated')
    list_editable = ['treated']
    
admin.site.register(Complain, ComplainAdmin)
# admin.site.unregister(Group)
