from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class History(models.Model):
    timer_date = models.DateTimeField(db_comment="Когда был использован таймер")
    timer_start = models.TimeField(db_comment="Когда был использован таймер")
    timer_end = models.TimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_history")