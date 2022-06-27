from email.mime import image
from email.policy import default
from inspect import classify_class_attrs
from multiprocessing.connection import answer_challenge
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User
import uuid

from pkg_resources import safe_extra

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro  = models.BooleanField(default=False)
    photo = models.ImageField(blank=True, default="static/avatar.jpg")
    tasks = models.ManyToManyField('Task', blank=True, default=None)

class typeTask(models.Model):
    COMP = (
        ('easy', 'Легко'),
        ('middle', 'Средне'),
        ('hard', 'Тяжело')
    )
    title = models.CharField(max_length=50, db_index=True)
    complexity = models.CharField(max_length=10, choices=COMP)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title
    
class subType(models.Model):
    type = models.ForeignKey(typeTask, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.title

class Task(models.Model):
    type = models.ForeignKey(subType, on_delete=models.PROTECT)
    traning = models.BooleanField(default=False)
    content = models.TextField(max_length =  500)
    answer = models.CharField(max_length=50)
    solution = models.TextField(max_length=500, blank=True)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return self.content[0:10]

class Decision(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey(typeTask, on_delete=models.PROTECT)
    content = models.TextField(max_length=10000)
    def __str__(self):
        return self.title
    