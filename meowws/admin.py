from django.contrib import admin

# Register your models here.
from .models import Meoww, MeowwLike


class MeowwLikeAdmin(admin.TabularInline):
    model = MeowwLike


class MeowwAdmin(admin.ModelAdmin):
    inlines = [MeowwLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']

    class Meta:
        model = Meoww


admin.site.register(Meoww, MeowwAdmin)
