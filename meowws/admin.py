from django.contrib import admin

# Register your models here.
from .models import Meoww


class MeowwAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']

    class Meta:
        model = Meoww


admin.site.register(Meoww, MeowwAdmin)
