from django.urls import path
from . import views

urlpatterns = [
    path('',views.bye,name='bye')
]