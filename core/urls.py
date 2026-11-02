from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('messages/', views.messages_view, name='messages'),
    path('messages/<int:user_id>/', views.messages_view, name='messages_with_user'),
    path('groups/', views.groups_view, name='groups'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('settings/', views.settings_view, name='settings'),
]