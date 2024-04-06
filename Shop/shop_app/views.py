from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product

def index(request):
    return render(request, 'shop_app/index.html')

def client_buy(request, client_id):
    client = Client.objects.get(pk=client_id)

    last_7_days = timezone.now() - timedelta(days=7)
    client_buy_last_7_days = Product.objects.filter(buy__client=client, buy__buy_data__gte=last_7_days).distinct()

    last_30_days = timezone.now() - timedelta(days=30)
    client_buy_last_30_days = Product.objects.filter(buy__client=client, buy__buy_data__gte=last_30_days).distinct()

    last_365_days = timezone.now() - timedelta(days=365)
    client_buy_last_365_days = Product.objects.filter(buy__client=client, buy__buy_data__gte=last_365_days).distinct()

    return render(request, 'shop_app/client_buy.html',{
        'client_buy_last_7_days': client_buy_last_7_days,
        'client_buy_last_30_days': client_buy_last_30_days,
        'client_buy_last_365_days': client_buy_last_365_days,
    })