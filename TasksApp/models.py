from django.db import models
from LoginApp.models import User

# Create your models here.

class TaskModel(models.Model):

    priority_choice = (
        ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='TasksApp', null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=priority_choice, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.create_date)