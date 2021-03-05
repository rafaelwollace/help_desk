from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Setor", {"fields": ("setor",)}),
        ("Unidade", {"fields": ("unidade",)}),
        ("Informações", {"fields": ("bio",)}),
    )

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)
