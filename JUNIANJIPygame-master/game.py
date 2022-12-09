import pygame.sprite

from player import Player
from voiture import Voiture
from voiture2 import Voiture2
from voiture3 import Voiture3
from voiture4 import Voiture4
from  voiture5 import Voiture5


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

    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


