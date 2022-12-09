import pygame.sprite

from player import Player
from voiture import Voiture
from voiture2 import Voiture2
from voiture3 import Voiture3
from voiture4 import Voiture4
from voiture5 import Voiture5
from crocodile import Crocodile
from kayak import Kayak
from kayak2 import Kayak2
from crocodile2 import Crocodile2
from barque import Barque



class Game:

    def __init__(self):
        #definir si notre jeu a commence ou pas
        self.is_playing = False
        # generer notre joueur
        self.player = Player(self)
        self.allVoitures = pygame.sprite.Group()
        self.pressed = {}
        self.spawnVoiture()
        self.spawnVoiture2()
        self.spawnVoiture3()
        self.spawnVoiture4()
        self.spawnVoiture5()
        self.spawnCrocodile()
        self.spawnKayak()
        self.spawnKayak2()
        self.spawnCrocodile2()
        self.spawnBarque()


    def spawnVoiture(self):
        voiture1 = Voiture(Game)
        self.allVoitures.add(voiture1)

    def spawnVoiture2(self):
        voiture2 = Voiture2(Game)
        self.allVoitures.add(voiture2)

    def spawnVoiture3(self):
        voiture3 = Voiture3(Game)
        self.allVoitures.add(voiture3)

    def spawnVoiture4(self):
        voiture4 = Voiture4(Game)
        self.allVoitures.add(voiture4)

    def spawnVoiture5(self):
        voiture5 = Voiture5(Game)
        self.allVoitures.add(voiture5)

    def spawnCrocodile(self):
        crocodile = Crocodile(Game)
        self.allVoitures.add(crocodile)

    def spawnKayak(self):
        kayak = Kayak(Game)
        self.allVoitures.add(kayak)

    def spawnKayak2(self):
        kayak2 = Kayak2(Game)
        self.allVoitures.add(kayak2)

    def spawnCrocodile2(self):
        crocodile2 = Crocodile2(Game)
        self.allVoitures.add(crocodile2)

    def spawnBarque(self):
        barque = Barque(Game)
        self.allVoitures.add(barque)

    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


