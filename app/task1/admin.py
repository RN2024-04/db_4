from django.contrib import admin
from .models import Game,Buyer

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter=('size', 'cost')
    list_display=('title', 'cost','size',)
    seach_fields=('title',)
    list_per_page=20
    fieldsets = (
        ('Game Info', {
            'fields': (('title', 'cost'), )
        }),
        ('Game', {
            'fields': ('description', ('size', 'age_limited'),)
        }),
    )



@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter=('balance', 'age')
    list_display=('name', 'balance','age',)
    seach_fields=('name',)
    list_per_page=30
    fields = [('name', 'balance', 'age')]

