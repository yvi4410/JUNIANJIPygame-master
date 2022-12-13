import time

import pygame

import gameover
from player import Player
from game import Game
from voiture import Voiture
from voiture2 import Voiture2
from kayak import Kayak
from kayak2 import Kayak2
pygame.init()

#creer une 1ere classe: notre joueur
#voir Class Player

#Generation fenetre de jeu
pygame.display.set_caption("Junianji 2022")
screen = pygame.display.set_mode((550, 650))

#import Background
background = pygame.image.load('Junianji Assets/Froggers Background.png')
background = pygame.transform.scale(background, (550, 650))

#gamover
class Gameover:
    gameover = pygame.image.load('Junianji Assets/Game Over.png')
    gameover = pygame.transform.scale(gameover, (400, 180))

#Charger notre jeu
game = Game()


running = True

#boucle tant que cette condition est vraie

while running:

    #appliquer le Background
    screen.blit(background, (0,0))
    #screen.blit(Gameover.gameover, (74, 230))

    #appliquer l image du joueur
    screen.blit(game.player.image, game.player.rect)

    #appliquer tout les projectiles
    game.player.allProjectile.draw(screen)

    #afficher les voitures
    game.allVoitures.draw(screen)

    #FAIRE AVANCER LES VOITURES ETC
    for Voiture in game.allVoitures:
        Voiture.move_right()

    #verifier si le joueur veut aller a gauche ou droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width <= screen.get_width() +10 :
        game.player.move_right()
        #changer l image quand on avance
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Right.png')
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= -10:
        game.player.move_left()
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Left.png')
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y >= 0:
        game.player.move_up()
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Up.png')
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y <= 599:
        game.player.move_down()
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Down.png')


    #LE JOUEUR AVANCE AVEC LES CANOE
    if game.player.rect.x > game.Kayak.rect.x and game.player.rect.x < game.Kayak.rect.x + 150 and game.player.rect.y < game.Kayak.rect.y + 90 and game.player.rect.y > game.Kayak.rect.y:
        game.player.rect.x = game.player.rect.x + 2

    if game.player.rect.x > game.Kayak2.rect.x and game.player.rect.x < game.Kayak2.rect.x + 150 and game.player.rect.y < game.Kayak2.rect.y + 90 and game.player.rect.y > game.Kayak2.rect.y:
        game.player.rect.x = game.player.rect.x + 2

    if game.player.rect.x > game.Crocodile.rect.x and game.player.rect.x < game.Crocodile.rect.x + 120 and game.player.rect.y < game.Crocodile.rect.y + 70 and game.player.rect.y > game.Crocodile.rect.y:
        game.player.rect.x = game.player.rect.x + 2

    if game.player.rect.x > game.Crocodile2.rect.x and game.player.rect.x < game.Crocodile2.rect.x + 120 and game.player.rect.y < game.Crocodile2.rect.y + 70 and game.player.rect.y > game.Crocodile2.rect.y:
        game.player.rect.x = game.player.rect.x + 2

    #time.sleep(0.005)

        #mettre l ecran a jour
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l event est fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est appuye
            if event.key == pygame.K_SPACE:
                game.player.launchProjectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False