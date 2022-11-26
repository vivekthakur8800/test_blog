from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    discription=models.TextField()

class Comment(models.Model):
    blogger=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)