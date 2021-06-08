# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.courses.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    # files = serializers.FileField()

    class Meta:
        model = Course
        fields = "__all__"
