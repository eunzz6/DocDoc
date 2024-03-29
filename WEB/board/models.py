from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    body = models.CharField(max_length=250)
    file = models.FileField(upload_to='media/')
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body}'
