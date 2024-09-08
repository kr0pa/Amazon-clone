from django.urls import path
from . import views

app_name='app_core'
urlpatterns =[
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product, name='product')
]