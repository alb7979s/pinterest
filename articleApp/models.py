from django.contrib.auth.models import User
from django.db import models
from projectApp.models import Project
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)
