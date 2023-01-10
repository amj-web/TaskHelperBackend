from django.db import models
from helper.models import TrackingModels
from authentication.models import User

class Category(TrackingModels):
    name =models.CharField(default='Learning',max_length=150,unique=True,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
         return self.name