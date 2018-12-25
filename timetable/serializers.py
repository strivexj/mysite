from rest_framework import serializers

from timetable.models import CoursesHtml


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesHtml
        fields = ('school', 'type', 'url', 'html')


class PostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CoursesHtml
        fields = ('school', 'contact', 'type', 'url', 'html')
