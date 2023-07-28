from django.contrib import admin
from users.models import User
from sneakers.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)

