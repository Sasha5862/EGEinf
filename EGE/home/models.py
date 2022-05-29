from email.mime import image
from inspect import classify_class_attrs
from multiprocessing.connection import answer_challenge
from tkinter import N
from django.db import models
import uuid

# Create your models here.
class typeTask(models.Model):
    COMP = (
        ('easy', 'Легко'),
        ('middle', 'Средне'),
        ('hard', 'Тяжело')
    )
    title = models.CharField(max_length=50, db_index=True)
    complexity = models.CharField(max_length=10, choices=COMP)
    id = models.AutoField(primary_key=True)
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.ForeignKey(typeTask, on_delete=models.PROTECT)
    content = models.TextField(max_length =  500)
    answer = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to="images/")