from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    message = models.TextField()


class Buddy(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buddies_1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buddies_2')
    active = models.BooleanField(default=False)