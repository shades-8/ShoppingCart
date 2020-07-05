from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('about/', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('tracking', views.tracking, name='tracking'),
    path('search', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<int:my_id>', views.products, name='products'),


]