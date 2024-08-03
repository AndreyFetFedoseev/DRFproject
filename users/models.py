from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course

NULLABLE = {"null": True, "blank": True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    surname = models.CharField(max_length=100, verbose_name="Отчество")
    phone = models.CharField(max_length=100, verbose_name="Телефон", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Город", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватарка", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    data_of_payment = models.CharField(max_length=100, verbose_name="Дата оплаты")
    paid_course = models.ManyToManyField(Course, verbose_name="Оплаченный курс")
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма оплаты", **NULLABLE)
    ChoicePayment = models.TextChoices("ChoicePayment", "cash transfer_to_account")
    payment_method = models.CharField(choices=ChoicePayment, max_length=30, verbose_name="Способ оплаты", **NULLABLE)

    def __str__(self):
        return f'{self.user} оплатил курсы: {self.paid_course}'

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
