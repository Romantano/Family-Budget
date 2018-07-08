from django.db import models
from datetime import date

from django.db.models import DecimalField


class Period(models.Model):
    name = models.CharField("Название:", max_length=30, null=True, help_text="Например: название месяца, номер  и т.п.")
    start_Date = models.DateField("Начало периода:", default=date.today)
    end_Date = models.DateField("Конец периода:", default=date.today)

    def __str__(self):
        return self.name


class CurrentBalance(models.Model):
    total = models.DecimalField("Текущий баланс", decimal_places=2, max_digits=10, blank=True)


class ChangeBalance(models.Model):
    sum = models.DecimalField("Сумма:", decimal_places=2, max_digits=10)
    name = models.CharField("Название:", max_length=50, null=True)
    category = models.CharField("Категория:", max_length=50, null=True)
    choises_balans = (
        ("Расход", "Расход"),
        ("Поступление", "Поступление")
    )
    change = models.CharField(max_length=12, choices=choises_balans, default="Расход")

 #   period = models.ForeignKey(Period)

    def __str__(self):
        return str(self.sum)



# Create your models here.
