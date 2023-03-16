from django.contrib import admin
from .models import Price, Portofolio_Item, Question, Portofolio_Photo, Message

admin.site.register(Price)
admin.site.register(Portofolio_Item)
admin.site.register(Portofolio_Photo)
admin.site.register(Question)
admin.site.register(Message)



admin.site.site_header = "SGC Design"
admin.site.site_title = "Baza de date"
admin.site.index_title = "Welcome to the Admin Panel"