from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "$%s" % (self.price / 100)
