from decimal import Decimal
from django import forms
from django.forms import RadioSelect
from django.shortcuts import render, redirect
from Planning.models import ChangeBalance, CurrentBalance


# Create your views here.


class ChangeBalanceForm(forms.ModelForm):
    class Meta:
        model = ChangeBalance
        fields = ('sum', 'name', 'category', 'change')


def index(request):
    try:
        cash = CurrentBalance.objects.get(id=1)
        print('OK')
    except:
        cash = CurrentBalance(id=1, total=Decimal(0.00))
        print('ошибка', cash.id, cash.total)
    if request.method == "POST":
        form = ChangeBalanceForm(request.POST)
        if form.is_valid():
            change_balance = ChangeBalance()
            data = form.cleaned_data
            change_balance.sum = data['sum']
            change_balance.name = data['name']
            change_balance.category = data['category']
            change_balance.change = data['change']
            change_balance.save()
            if data['change'] == 'Расход':
                cash.total -= data['sum']
            else:
                cash.total += data['sum']
            print(cash.total)
            cash.save()
            return redirect("/")
    else:
        form = ChangeBalanceForm(initial={"change": RadioSelect})
    table = ChangeBalance.objects.all()
    print(table)
    return render(request, "index.html", {'form': form, 'total': cash.total, 'table': table})
