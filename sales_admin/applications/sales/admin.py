from django.contrib import admin

from applications.warehouse.models import Currency

# Agregamos al modelo Currency al django admin
admin.site.register(Currency)
