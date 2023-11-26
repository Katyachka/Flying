from django.db import models


# Create your models here.

class User(models.Model):
    chat_id = models.IntegerField(
        verbose_name="Чат",
        null=False
    )
    user_info_id = models.ForeignKey(
        to="botapp.UserInfo",
        verbose_name="Інформація о користувачі",
        on_delete=models.PROTECT,
        null=True
    )
    save_info = models.BooleanField(
        verbose_name="Зберегти особисті данні ?"
    )
    ticket = models.ManyToManyField("botapp.Ticket")

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class UserInfo(models.Model):
    name = models.TextField(
        verbose_name="Ім'я користувача",
        null=False
    )
    surname = models.TextField(
        verbose_name="Прізвище користувача",
        null=False
    )
    sex = models.TextField(
        verbose_name="Стать",
        null=False
    )
    phone_number = models.TextField(
        verbose_name="Номер телефону",
        null=False
    )
    email = models.TextField(
        verbose_name="Електронна пошта",
        null=False
    )

    class Meta:
        verbose_name = "Інформація про користувача"
        verbose_name_plural = "Інформація про користувачів"


class Plane(models.Model):
    model = models.TextField(
        verbose_name="Модель",
        null=False
    )
    passengers = models.IntegerField(
        verbose_name="Пасажири",
        null=False
    )
    plane_layout = models.BinaryField(
        verbose_name="Розташування місць",
        null=False
    )

    class Meta:
        verbose_name = "Літак"
        verbose_name_plural = "Літаки"


class Flight(models.Model):
    plane_id = models.ForeignKey(
        to="botapp.Plane",
        verbose_name="Літак",
        null=False,
        on_delete=models.PROTECT
    )
    departure = models.TextField(
        verbose_name="Аеропорт відправки",
        null=False
    )
    arrival = models.TextField(
        verbose_name="Аеропорт прибуття",
        null=False
    )
    departure_date_time = models.DateTimeField(
        verbose_name="Дата та час відправки",
        null=False
    )
    arrival_date_time = models.DateTimeField(
        verbose_name="Дата та час прибуття",
        null=False
    )
    duration = models.DurationField(
        verbose_name="Тривалість",
        null=False
    )
    cost_base = models.IntegerField(
        verbose_name="Базова вартість",
        null=False
    )
    cost_regular = models.IntegerField(
        verbose_name="Вартість до 10 кг багажу",
        null=False
    )
    cost_plus = models.IntegerField(
        verbose_name="Вартість до 20 кг багажу",
        null=False
    )

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейси"


class Seat(models.Model):
    number = models.TextField(
        verbose_name="Но",
        null=False
    )
    user_info_id = models.ForeignKey(
        to="botapp.UserInfo",
        verbose_name="",
        on_delete=models.PROTECT,
        null=False
    )
    flight_id = models.ForeignKey(
        to="botapp.Flight",
        verbose_name="",
        on_delete=models.PROTECT,
        null=False
    )

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"


class Ticket(models.Model):
    flight_id = models.ForeignKey(
        to="botapp.Flight",
        verbose_name="",
        on_delete=models.PROTECT,
        null=False
    )
    plane_id = models.ForeignKey(
        to="botapp.Plane",
        verbose_name="",
        null=False,
        on_delete=models.PROTECT
    )
    seat_id = models.ForeignKey(
        to="botapp.Seat",
        verbose_name="",
        on_delete=models.PROTECT,
        null=False
    )

    class Meta:
        verbose_name = "Білет"
        verbose_name_plural = "Білети"