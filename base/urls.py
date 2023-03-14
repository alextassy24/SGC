from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portofolio/', views.portofolio, name='portofolio'),
    path('prices/', views.price_list, name='prices'),
    path('products/<str:pk>', views.products, name='product'),
    
    
]