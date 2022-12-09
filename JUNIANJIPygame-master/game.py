import pygame.sprite

from player import Player
from voiture import Voiture
from voiture2 import Voiture2


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

    def spawnVoiture(self):
        voiture1 = Voiture(Game)
        self.allVoitures.add(voiture1)

    def spawnVoiture2(self):
        voiture2 = Voiture2(Game)
        self.allVoitures.add(voiture2)


    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


