from django.contrib import admin
from .models import Character, Region, Type, Weapon, Constellation, VoiceActor, Country


@admin.register(Character)
class Character(admin.ModelAdmin):
    pass


@admin.register(Country)
class Country(admin.ModelAdmin):
    pass


@admin.register(Region)
class Region(admin.ModelAdmin):
    pass


@admin.register(Type)
class Type(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class Weapon(admin.ModelAdmin):
    pass


@admin.register(Constellation)
class Constellation(admin.ModelAdmin):
    pass


@admin.register(VoiceActor)
class Constellation(admin.ModelAdmin):
    pass
