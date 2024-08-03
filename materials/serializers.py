from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson = SerializerMethodField()

    def get_count_lesson(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    def get_lesson(self, obj):
        return [lesson.title for lesson in Lesson.objects.filter(course=obj.pk)]

    class Meta:
        model = Course
        fields = ("title", "preview", "description", "count_lesson", "lesson",)


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
