from django.db import models

class Jugadores(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    numero_camiseta = models.IntegerField()
    Minibasket = "U10/U12"
    SubTrece = "U13"
    Infantil = "U15"
    Cadete = "U17"
    Juvenil = "U19"
    Primera = "U21/+"
    categoria = [
        (Minibasket, "Minibasket"),
        (SubTrece, "SubTrece"),
        (Infantil, "Infantil"),
        (Cadete, "Cadete"),
        (Juvenil, "Juvenil"),
        (Primera, "Primera"),
    ]
    actualmente_juega_en = models.CharField(
        max_length=10,
        choices=categoria,
        default=Minibasket,
    )
    def is_upperclass(self):
        return self.actualmente_juega_en in {self.Minibasket, self.SubTrece, self.Infantil, self.Cadete, self.Juvenil, self.Primera}
    
class Entrenadores(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField()
    trayectoria = models.CharField(max_length=200)

class Clubes(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion_club = models.TextField()