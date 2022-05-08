from re import M
from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    tesk = models.TextField('Description')

    def __str__(self):
        return self.title