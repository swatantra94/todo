from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=1024)
    description = models.TextField()


    def __str__(self):
        return self.title

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post= models.ForeignKey('Todolist',on_delete=models.CASCADE)
    likes = models.BooleanField(default=0)
