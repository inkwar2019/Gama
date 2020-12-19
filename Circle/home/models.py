from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='post/')
    price = models.DecimalField(decimal_places=2,max_digits=7,default="0")
    discount = models.DecimalField(decimal_places=2,max_digits=5,default="0")
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output = (300,300)
            img.thumbnail(output)
            img.save(self.image.path)


class Notification(models.Model):
    title = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.TextField(default="NoUser")
    confirmed = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    