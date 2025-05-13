import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import VintPlayer, PlayerFromVint


# Create your views here.
def index(request):
    return render(request, "vint/index.html")

def player_list(request):
    online_players  = list(VintPlayer.objects.filter(is_online=True).values_list('username', flat=True))
    all_players     = PlayerFromVint.objects.all().exclude(username__in=online_players).values('username')
    return render(request, "vint/players.html", context={
        "server_active": True,
        "all_players": all_players,
        "online_players": online_players,
    })
    # return JsonResponse(players, safe=False)

def game(request):
    return render(request, "vint/game.html")
def media_page(request):
    return render(request, "vint/media.html")
def forum_page(request):
    return render(request, "vint/forum.html")
def login_vint(request):
    return render(request, "vint/login.html")

@csrf_exempt
def player_online(request):
    if request.method == "POST":
        username  = request.POST.get("username")
        is_online = request.POST.get("status") == "online"

        print("username:", username)
        print("is_online:", is_online)

        if username:
            player, vp_created = VintPlayer.objects.get_or_create(username=username)
            player.make_vint_online(is_online)

        return JsonResponse({"status": "ok"})
