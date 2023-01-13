from django.db import models

from django.db import models

class TrackingModels(models.Model):
    # created_at field will store the date and time when the object is created
    created_at=models.DateTimeField(auto_now_add=True)
    # updated_at field will store the date and time when the object is updated
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        # This class is an abstract class, it will not create a table
        abstract=True
        # By default, it will order the objects in descending order based on the created_at field
        ordering=("-created_at",)
