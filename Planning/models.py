from django.db import models
from datetime import date


class Period(models.Model):
    name = models.CharField("Название:", max_length=30, null=True, help_text="Например: название месяца, номер  и т.п.")
    start_Date = models.DateField("Начало периода:", default=date.today)
    end_Date = models.DateField("Конец периода:", default=date.today)

    def __str__(self):
        return self.name


class CurrentBalance(models.Model):
    total = models.CharField("Текущий баланс", default=0, max_length=10)


class ChangeBalance(models.Model):
    sum = models.DecimalField("Сумма:", decimal_places=2, max_digits=10)
    name = models.CharField("Название:", max_length=30, null=True)
    category = models.CharField("Категория:", max_length=30, null=True)
    date = models.DateField("Дата")
    choises_balans = (
        ("Spending", "Расход"),
        ("Income", "Поступление")
    )
    change = models.CharField(max_length=8, choices=choises_balans, default="Income")

    period = models.ForeignKey(Period)

    def __str__(self):
        return self.get_change_display() + ': ' + str(self.sum)

# Create your models here.
