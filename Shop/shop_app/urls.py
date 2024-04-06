from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('client_buy/', views.client_buy, name='client_buy'),
]
