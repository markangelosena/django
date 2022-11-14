from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play


# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("lastname","firstname","height","weight")
    search_fields = ("lastname",)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name","coach",)
    search_fields = ("name",)

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("player","team","string_no","isActive",)