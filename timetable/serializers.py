from rest_framework import serializers

from timetable.models import CoursesHtml


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesHtml
        fields = ('school', 'type', 'html')
