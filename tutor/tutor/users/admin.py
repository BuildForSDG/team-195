from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

# from tutor.users.forms import UserChangeForm, UserCreationForm # form replaced with serializers

# from .models import User, Student # new
from .models import Student # new
from django.contrib.auth.models import Group



User = get_user_model()


@admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
class UserAdmin(BaseUserAdmin):
    """
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    """

    # new=====
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_instructor', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_instructor', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_instructor']
    search_fields = ('email', 'username')
    ordering = ('email',)

    ##====


# new
# admin.site.register(Student)
# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
