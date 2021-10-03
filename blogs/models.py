from django.db import models
from django.contrib.auth.models import User 

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    maalik = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

