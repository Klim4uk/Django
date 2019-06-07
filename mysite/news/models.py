from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length= 120)
    post = models.TextField()
    data = models.DateTimeField()
    foto = models.TextField()

    def __str__(self):
        return self.title


