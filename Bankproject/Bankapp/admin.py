from django.contrib import admin

from .models import District, Branch, Customer, Material

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Material)