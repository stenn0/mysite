from django.db import models

class PlayerFromVint(models.Model):
    id          = models.IntegerField(primary_key=True)
    username    = models.CharField(max_length=256, unique=True)
    email       = models.EmailField(unique=True)
    crystals    = models.IntegerField()
    xcrystals   = models.IntegerField()
    experience  = models.IntegerField()

    class Meta:
        app_label = 'vint'
        default_permissions = ()

    def __str__(self):
        return self.username


class VintPlayer(models.Model):
    username = models.CharField(max_length=256, unique=True)
    is_online = models.BooleanField(default=False)
    player_id = models.BigIntegerField(unique=True)  # PlayerFromVint.id

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.username

    def sync_player_id(self):
        try:
            player = PlayerFromVint.objects.get(username=self.username)
            self.player_id = player.id
        except PlayerFromVint.DoesNotExist:
            raise ValueError(f"Користувача з username='{self.username}' не знайдено у vint.Players")

    def sync_username_from_vint(self):
        """Оновлює username цього об’єкта згідно з PlayerFromVint"""
        try:
            player = PlayerFromVint.objects.get(id=self.player_id)
            if self.username != player.username:
                self.username = player.username
                self.save(update_fields=["username"])
        except PlayerFromVint.DoesNotExist:
            raise ValueError(f"Не знайдено гравця з id={self.player_id} у vint.Players")
        
    def make_vint_online(self, status=True):
        """Встановлює онлайн статус"""
        self.is_online = status
        self.save(update_fields=["is_online"])

    def save(self, *args, **kwargs):
        if not self.player_id:
            self.sync_player_id()
        super().save(*args, **kwargs)
