from django.db import models
from django.utils import timezone


class CoursesHtml(models.Model):
    created = models.DateTimeField(default=timezone.now)
    school = models.CharField(max_length=25)
    type = models.CharField(max_length=10, default='adaptation')
    url = models.CharField(max_length=100, default='#')
    html = models.TextField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.school
