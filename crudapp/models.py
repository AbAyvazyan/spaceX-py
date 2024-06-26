from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)

    def __str__(self):
        return self.title