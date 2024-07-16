from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def clean(self):
        # Ensure the due date is in the future
        if self.due_date <= timezone.now():
            raise ValidationError('Due date must be in the future.')
        
    def __str__(self):
        return self.title
