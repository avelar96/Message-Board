from django.db import models

class Post(models.Model):
    title = models.TextField(unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
