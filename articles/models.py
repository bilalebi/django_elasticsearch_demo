from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    abstract = models.TextField(null=False)
    link = models.CharField(max_length=255)
    conclusion = models.TextField(null=False)

    def __str__(self):
        return f'{self.title}'
