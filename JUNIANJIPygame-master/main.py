import pygame
from player import Player
from game import Game
from voiture import Voiture
from voiture2 import Voiture2
pygame.init()

#creer une 1ere classe: notre joueur
#voir Class Player

#Generation fenetre de jeu
pygame.display.set_caption("Junianji 2022")
screen = pygame.display.set_mode((550, 650))

#import Background
background = pygame.image.load('Junianji Assets/Froggers Background.png')
background = pygame.transform.scale(background, (550, 650))

#Charger notre jeu
game = Game()


running = True

#boucle tant que cette condition est vraie

while running:

    #appliquer le Background
    screen.blit(background, (0,0))

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
    elif game.pressed.get(pygame.K_UP):
        game.player.move_up()
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Up.png')
    elif game.pressed.get(pygame.K_DOWN):
        game.player.move_down()
        game.player.image = pygame.image.load('Junianji Assets/Froggers Final Down.png')

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