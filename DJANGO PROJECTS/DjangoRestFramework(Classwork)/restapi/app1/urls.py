from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.item_list, name='item_list_api'),
    path('api/items/<int:pk>/', views.item_detail, name='item_detail_api'),
    path('items/', views.item_list_view, name='item_list'),
    path('items/create/', views.item_create_view, name='item_create'),
    path('items/<int:pk>/', views.item_detail_view, name='item_detail'),
    path('items/<int:pk>/edit/', views.item_update_view, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete_view, name='item_delete'),
]