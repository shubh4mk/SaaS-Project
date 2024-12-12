from django.db import models

# Create your models here.
class PageVisits(models.Model):
    # db -> table
    # hidden col -> id -> Primary Key -> autofield -> 1, 2, 3
    path = models.TextField() # col
    timestamp = models.DateTimeField(auto_now_add=True) # col