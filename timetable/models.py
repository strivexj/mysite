from django.db import models
from django.utils import timezone


class CoursesHtml(models.Model):
    created = models.DateTimeField(default=timezone.now)
    school = models.CharField(max_length=25)
    contact = models.CharField(max_length=25, default="选填")
    type = models.CharField(max_length=10, default='Adaptation')
    url = models.CharField(max_length=100, default='#')
    html = models.TextField()
    valid = models.BooleanField(default=True)
    adapted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    eas = models.CharField(max_length=25, default='Unknown')

    class Meta:
        ordering = ("read", "adapted", "-type", "-valid", "created")

    def __str__(self):
        return self.school
