from django.urls import path
from . import views

urlpatterns = [
    path("",                views.game,            name='game'),           # головна Vint
    path('players/',        views.player_list,      name='player_list'),
    # path('game/',           views.game,             name='game'),
    path('media/',          views.media_page,       name='media'),
    path('forum/',          views.forum_page,       name='forum'),
    path('login/',          views.login_vint,       name='login'),

    path("api/player-online/",  views.player_online,    name="player_online"),  # API для перевірки онлайн-статусу гравця
]
