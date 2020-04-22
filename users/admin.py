from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = (
    'username', 'is_student', 'is_teacher', 'is_staff', 'is_active')
    list_filter = (
    'username', 'is_student', 'is_teacher',  'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'date_joined')}),
        ('Роли', {'fields': (
        'is_student', 'is_teacher', 'is_active', 'is_staff')})
    )
    search_fields = ('username',)
    readonly_fields = ['date_joined']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_student', 'is_teacher', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Users, CustomUserAdmin)


