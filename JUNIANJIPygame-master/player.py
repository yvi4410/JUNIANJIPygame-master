import pygame.sprite
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 500
        self.velocity = 5
        self.allProjectile = pygame.sprite.Group()
        self.image = pygame.image.load('Junianji Assets/Froggers Final Up.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 600

    screenGameOver = pygame.display.set_mode((550, 650))
    gameover = pygame.image.load('Junianji Assets/Game Over.png')


    def move_right(self):
        #si le ptit bonhomme est pas en collision avec une tuture
        if not self.game.checkCollision(self, self.game.allVoitures):
            self.rect.x += self.velocity
        else:
            ...

    def move_left(self):
        if not self.game.checkCollision(self, self.game.allVoitures):
            self.rect.x -= self.velocity
        else:
            ...

    def move_up(self):
        if not self.game.checkCollision(self, self.game.allVoitures):
            self.rect.y -= self.velocity
        else:
            ...

    def move_down(self):
        if not self.game.checkCollision(self, self.game.allVoitures):
            self.rect.y += self.velocity
        else:
            ...

    def launchProjectile(self):
        #creer une nvle instance de la classe projectile
        self.allProjectile.add(Projectile(self))

