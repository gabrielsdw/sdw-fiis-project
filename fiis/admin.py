from django.contrib import admin
from . import models

@admin.register(models.Fii)
class FiiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dividends',)
    search_fields = ('name',)


