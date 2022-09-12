from django.contrib import admin

from api_stripe.models import Item


@admin.register(Item)
class ItemManager(admin.ModelAdmin):
    pass
