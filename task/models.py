from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_PRIORITY_CHOICES = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    TASK_TYPE_CHOICES = [('Individual', 'Individual'), ('Team', 'Team')]

    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    task_priority = models.CharField(max_length=50, choices=TASK_PRIORITY_CHOICES)
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default='Individual')  # ✅ Add this line
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title

class TaskAssignment(models.Model):
    employee_name = models.CharField(max_length=100,default='')  # Directly store employee name

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_assigned")  
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_given")  
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.task.task_title} - {self.assigned_to.username}"



