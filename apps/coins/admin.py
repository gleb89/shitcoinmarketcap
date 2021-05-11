from django.contrib import admin
from .models import Coins, Exchange

# admin.site.register(Coins)

admin.site.register(Exchange)
@admin.register(Coins)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ('symbol','image', 'name', 'price', 'market_cap', 'volume')

    search_fields = ('symbol', 'name')
    ordering = ('-updated',)
    fields = (
        'symbol',
        'name',
        'description',
        'price',
        'market_cap',
        'volume',
        'market_exchange',
        'image',
        'price_exc',
        'board_price'
        )