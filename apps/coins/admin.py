from django.contrib import admin
from .models import Coins, Exchange,Note

admin.site.register(Coins)
admin.site.register(Note)
admin.site.register(Exchange)

