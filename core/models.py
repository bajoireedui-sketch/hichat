from django.db import models
from django.contrib.auth.models import User

# Хэрэглэгчийн нэмэлт мэдээлэл (Аватар, био, статус)
class Profile(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('away', 'Away'),
        ('offline', 'Offline'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="IT & AI Student | Passionate about building awesome web products.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    avatar_color = models.CharField(max_length=20, default='bg-primary')

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Хувийн чатны мессежүүд
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}: {self.content[:20]}"

# Групп чатны модел
class GroupSpace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color_class = models.CharField(max_length=20, default='bg-primary')
    members = models.ManyToManyField(User, related_name='group_spaces')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name