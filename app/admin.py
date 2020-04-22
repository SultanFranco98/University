from django.contrib import admin
from .models import *

admin.site.site_header = "Единое окно"

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10
    save_as_continue = True


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty']
    list_filter = ['title', 'faculty']
    search_fields = ['title']
    list_per_page = 10
    save_as_continue = True


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'speciality']
    list_filter = ['title', 'speciality']
    search_fields = ['title']
    list_per_page = 10
    save_as_continue = True

class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'faculty', 'speciality', 'group', 'phone']
    list_filter = ['full_name', 'faculty', 'speciality', 'group', 'gender']
    search_fields = ['full_name']
    list_per_page = 10
    save_as_continue = True

admin.site.register(Facultys, FacultyAdmin)
admin.site.register(Specialitys, SpecialityAdmin)
admin.site.register(Groups, GroupAdmin)
admin.site.register(Students, StudentAdmin)