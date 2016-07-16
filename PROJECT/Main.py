#Unfair Mario Game
#Authors: Jon A., Andrew B., Peter V., Bri S.
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
pygame.key.set_repeat(50, 50)
from pygame.locals import *
import GameLogic
from GameLogic import Game,Graph

pygame.display.set_caption("Demo")

#Define event loop
def eventLoop():
    #set variables for radius and center
    center = [200,200]
    radius = 50

    #for redrawing
    drawCircle = True
    pygame.key.set_repeat(50, 50)
# move the character

    while True:
    # event hanlding loop
        eventList = pygame.event.get()
    # grab all events pygame recieved
        for event in eventList:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
            # if someone presses some key
            # <event.key> key attribute of a key-down event encodes which key is pressed
            # move the hero accordingly
                if event.key == pygame.K_LEFT:
                    GameLogic.x -= 10
                elif event.key == pygame.K_RIGHT:
                    GameLogic.x += 10

            pygame.draw.circle(screen,(130,30,250), center, radius)
            
            # move the hero to this position
           
           
    # The main game logic block
    
    # interactive objects
    GameLogic.updateGame()

    GameLogic.draw(screen)
    
    clock.tick(60)
    #60 updates in one second
    
    #update the display
    pygame.display.flip()
        #fill screen
    screen.fill ((0, 0, 0))
eventLoop()