from django.db import models
from django.forms import DateTimeField
from cloudinary.models import CloudinaryField



# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = "post"
    name=models.CharField('Name',max_length=50, blank=False, null = False, default="Anonymous", db_index=True )

    body = models.CharField('Body', max_length=200, blank=True, null=True) 

    created_at = models.DateTimeField('Created DataTime', blank=True, auto_now_add = True)

    image = CloudinaryField(
        'image', blank=True,
    )

    likes = models.PositiveIntegerField(
        'Likes', default=0, null=True, blank=True
    )