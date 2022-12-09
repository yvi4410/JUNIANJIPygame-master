import pygame.sprite
from contract.ivehicles import IVehicles
class Voiture4(pygame.sprite.Sprite):

    def move(self):
        pass

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 3
        self.image = pygame.image.load('Junianji Assets/voiture 9.png')
        self.image = pygame.transform.scale(self.image, (90, 55))
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = 400

    def move_right(self):
        #collision avec un groupe de joueur
        if self.rect.x > 700:
            self.rect.x = -200
        self.rect.x += self.velocity
