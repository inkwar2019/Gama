from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

dept = (
    ('CSE','CSE'),
    ('EEE','EEE'),
    ('ECE','ECE'),
    ('ETE','ETE'),
    ('ME','ME'),
    ('CE','CE'),
    ('CFPE','CFPE'),
    ('MTE','MTE'),
    ('GCE','GCE'),
    ('BMCSE','BMCSE'),
    ('Architecture','Architecture'),
)
yr = (
    ('first','first'),
    ('second','second'),
    ('third','third'),
    ('fourth','fourth'),
)
sem = (
    ('odd','odd'),
    ('even','even')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    p_number = models.CharField(max_length=11,default='01')
    department = models.CharField(choices=dept,max_length=20,default='CSE')
    year = models.CharField(choices=yr,max_length=20,default='first')
    semister = models.CharField(choices=sem,max_length=20,default='odd')
    image = models.ImageField(default='./profile_pics/default.png',upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output = (300,300)
            img.thumbnail(output)
            img.save(self.image.path)
    
class Support(models.Model):
    suggetion = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def get_absolute_url(self):
        return reverse('home')