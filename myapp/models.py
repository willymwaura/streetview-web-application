from django.db import models
from datetime import datetime

# Create your models here.
class Search(models.Model):
    title=models.CharField(max_length=100)
    