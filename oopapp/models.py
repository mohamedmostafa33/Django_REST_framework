from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)

class Magazine(models.Model):
    title = models.CharField(max_length = 200)
    publisher = models.CharField(max_length = 200)
    issue_numer = models.IntegerField()