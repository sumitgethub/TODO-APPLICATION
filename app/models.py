from django.db import models

from User.models import User

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    title = models.CharField(max_length=10)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title