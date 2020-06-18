from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('acceder/', views.login, name='login'),
    path('registro/', views.register, name='register'),
]
