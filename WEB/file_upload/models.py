from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    file = models.FileField()
    file2 = models.FileField(upload_to='wearable/')
    createDate = models.DateTimeField(auto_now_add=True)
class Submit(models.Model):
    file = models.FileField(upload_to='submit/')
    