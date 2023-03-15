from django.contrib import admin
from .models import Price, Portofolio_Item, Question

admin.site.register(Price)
admin.site.register(Portofolio_Item)
admin.site.register(Question)


admin.site.site_header = "SGC Design"
admin.site.site_title = "Baza de date"
admin.site.index_title = "Welcome to the Admin Panel"