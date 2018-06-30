from django.contrib import admin
from .models import Period, CurrentBalance, ChangeBalance


class PeriodAdmin(admin.ModelAdmin):
    list_display = ("name", "start_Date", "end_Date")


class ChangeBalanceAdmin(admin.ModelAdmin):
    list_display = ("sum", "category", "change")


admin.site.register(Period, PeriodAdmin)
admin.site.register(CurrentBalance)
admin.site.register(ChangeBalance, ChangeBalanceAdmin)
# Register your models here.
