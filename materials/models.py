from django.db import models


NULLABLE = {"null": True, "blank": True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/course", verbose_name="Картинка", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Название курса"
    )
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    preview = models.ImageField(
        upload_to="materials/course", verbose_name="Картинка", **NULLABLE
    )
    link_to_video = models.TextField(verbose_name="Ссылка на видео", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
