from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home' ),
    path('listing/',views.listing_list, name='listing'),
    path('listing/<int:pk>',views.listing_retrieve, name='listing_retrieve'),
    path('listing/create/', views.listing_create, name='listing_create'),
    path('listing/update/<int:pk>', views.listing_update, name='listing_update'),
    path('listing/delete/<int:pk>', views.listing_delete, name='listing_delete'),

]