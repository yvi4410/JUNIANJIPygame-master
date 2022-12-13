import pygame
import time

class Gameover:

    def __init__(self):
        self.screenG = pygame.display.set_mode((550, 650))
        self.gameover = pygame.image.load('Junianji Assets/Game Over.png')
        self.gameover = pygame.transform.scale(self.gameover, (400, 180))

    def gameOver(self):
        self.screenG.blit(self.gameover, (74, 230))
        time.sleep(2)