from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def status(request):
    list_watchlist = WatchlistItem.objects.all()
    cnt = 0
    for watchlist in list_watchlist:
        if watchlist.watched == "True":
            cnt += 1
    if cnt >= len(list_watchlist) - cnt:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"

def show_watchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'list': data_watchlist,
        'nama': 'Muhammad Abizar Rachmanda',
        'id' : '2106751133',
        'status' : status(request)
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_item_by_id(request):
    data_watchlist = WatchlistItem.objects.filter(pk=id)
    context = {
        'list': data_watchlist,
        'nama': 'Muhammad Abizar Rachmanda',
        'id' : '2106751133',
    }
    return render(request, "mywatchlist.html", context)
