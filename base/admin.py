from django.contrib import admin
from .models import Prices, Portofolio

admin.site.register(Prices)
admin.site.register(Portofolio)

admin.site.site_header = "SGC Design"
admin.site.site_title = "Baza de date"
admin.site.index_title = "Welcome to the Admin Panel"