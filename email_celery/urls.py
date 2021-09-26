from django.urls import path 
from . import views

app_name = 'email_celery'

urlpatterns = [
    path('celery/', views.index, name='index'),
]