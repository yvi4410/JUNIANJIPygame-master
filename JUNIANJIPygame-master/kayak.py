import pygame.sprite
from contract.ivehicles import IVehicles
class Kayak(pygame.sprite.Sprite):

    def move(self):
        pass

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 2
        self.image = pygame.image.load('Junianji Assets/kayak.png')
        self.image = pygame.transform.scale(self.image, (150, 90))
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = 175
        self.azeaze = 2

    def move_right(self):
        #collision avec un groupe de joueur
        if self.rect.x > 700:
            self.rect.x = -200
        self.rect.x += self.velocity
