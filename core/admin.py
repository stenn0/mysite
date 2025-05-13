from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from vint.models import VintPlayer, PlayerFromVint


@admin.register(PlayerFromVint)
class PlayerFromVintAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'crystals', 'xcrystals', 'experience')
    search_fields = ('username', 'email')


@admin.register(VintPlayer)
class VintPlayerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'is_online',
    )
    readonly_fields = (
        'player_id',
    )
    search_fields = ('username',)
    list_filter = ('is_online',)
