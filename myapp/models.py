from django.db import models
from django.forms import ModelForm

# Create your models here.
index_label=(('1', 'Problem 1'), ('2', 'Problem 2'), ('3', 'Problem 3'))
# Create your models here.
class User(models.Model):
    headimg = models.FileField(upload_to="media/img")
    label = models.CharField(max_length=2, choices=index_label)
    diag = models.CharField(max_length=500)
    # 返回名

def __str__(self):
    return self.name
