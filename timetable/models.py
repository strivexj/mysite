from django.db import models


class CoursesHtml(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=25)
    type = models.CharField(max_length=10)
    html = models.TextField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.school
