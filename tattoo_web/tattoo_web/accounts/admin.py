from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email',)
    search_fields = ['username']
    ordering = ('pk',)
    # exclude = ['password', 'is_superuser']
    readonly_fields = ('username', 'date_joined', 'last_login', 'password', 'is_superuser')

    fieldsets = (
        ('User Info', {'fields': ('username', 'email', 'password', 'is_active',)}),
        ('Profile Info', {'fields': ('first_name', 'last_name', 'profile_picture',)}),
        ('Staff', {'fields': ('is_superuser', 'is_staff', 'groups', 'user_permissions',)}),
        ('Timeline', {'fields': ('date_joined', 'last_login',)}),
    )
