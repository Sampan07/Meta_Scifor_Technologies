from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app1.urls')),
    path('items/', include('app1.urls')),
    path('', views.home_view, name='home'),
]
