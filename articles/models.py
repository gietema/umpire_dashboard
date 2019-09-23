from django.db import models

from users.models import User
from umpire_dashboard import settings

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')