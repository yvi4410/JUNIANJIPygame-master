import time
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
        self.rect.x = 225
        self.rect.y = 600
    screenGameOver = pygame.display.set_mode((550, 650))
    gameover = pygame.image.load('Junianji Assets/Game Over.png')

    def death(self):
        self.rect.y = 600
        self.rect.x = 225
        print("Game Over")
        time.sleep(2)


    def move_right(self):
        #si le ptit bonhomme est pas en collision avec une tuture
        if self.rect.y >= 265:
            if not self.game.checkCollision(self, self.game.allVoitures):
                self.rect.x += self.velocity
            else:
                self.death()
        elif self.rect.y <= 265:
            print("Plouf")
            self.death()

    def move_left(self):
        if self.rect.y >= 265:
            if not self.game.checkCollision(self, self.game.allVoitures):
                self.rect.x -= self.velocity
            else:
                self.death()
        elif self.rect.y <= 265:
            print("Plouf")
            self.death()

    def move_up(self):
        if self.rect.y >= 265:
            if not self.game.checkCollision(self, self.game.allVoitures):
                self.rect.y -= self.velocity
            else:
                self.death()
        elif self.rect.y <= 265:
            print("Plouf")
            self.death()

    def move_down(self):
        if self.rect.y >= 265:
            if not self.game.checkCollision(self, self.game.allVoitures):
                self.rect.y += self.velocity
            else:
                self. death()
        elif self.rect.y <= 265:
            print("Plouf")
            self.death()

    def launchProjectile(self):
        #creer une nvle instance de la classe projectile
        self.allProjectile.add(Projectile(self))