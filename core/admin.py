from django.contrib import admin
from .models import Profile, Message, GroupSpace

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'avatar_color')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')

@admin.register(GroupSpace)
class GroupSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')