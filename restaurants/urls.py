from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants_index, name='restaurants_index'),
]

urlpatterns += [
    path('diners/', views.dinersButton, name='diners'),
]

urlpatterns += [
    path('q/', views.dinersButton, name='results'),
]

urlpatterns += [
    path('maps/', views.maps, name='maps'),
]