from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User,related_name = "messages",on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        print(f"{self.username} - {self.message}")
class UserAnalytics(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    message_count = models.BigIntegerField(default=0)
    def __str__(self):
        print(f"{self.username} - {self.message_count}")