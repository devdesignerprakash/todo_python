from django.db import models

class TaskManager(models.Model):
    name=models.CharField( max_length=50)
    desc=models.TextField()
    deadline=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created
    updated_at = models.Date(auto_now=True)


    def __stir__(self):
        self.name
# Create your models here.
