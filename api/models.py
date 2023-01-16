from django.db import models
from helper.models import TrackingModels
from authentication.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
TASK_STATUS = [("OPEN", "Open"), ("CLOSED", "Closed"), ("IN-PROGRESS", "InProgress"), ("BLOCKED", "Blocked"),("COMPLETED","Completed")]
PRIORITY_STATUS= [("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High"), ("OPTIONAL", "Optional")]

# Category model to save categories
class Category(TrackingModels):
    name =models.CharField(default='zyn',max_length=150,unique=False,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
         return self.name

# Todo model for saving the todos
class ToDo(TrackingModels):

     title = models.CharField(max_length=150,blank=False,unique=True,null=False)
     description=models.TextField()
     image = CloudinaryField('image', default=None,blank=True,null=True)
     dueDate=models.DateField(blank=False,null=False)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     assigned=models.CharField(max_length=150,blank=True,null=True)
     status=models.CharField(max_length=150,choices=TASK_STATUS, default="OPEN")
     priority=models.CharField(max_length=150,choices=PRIORITY_STATUS, default="LOW")
     category=models.ForeignKey(Category, on_delete=models.CASCADE)

     def __str__(self):
          return self.title