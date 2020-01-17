import pygame
import random
import time
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('Monkey Fever')
screen.fill((0,0,255))

pygame.draw.rect(screen,(255,0,0),(200,150,100,50))

pygame.draw.circle(screen,(250,0,0),(10,10),25)
background = pygame.Surface(screen.get_size())
background = background.convert()
pygame.draw.polygon(screen,(255,0,255),((146,0),(291,106),(236,277),(56,277),(0,106))



while True:
    for event in pygame.event.get():
        if event.type == exit():
            pygame.quit()
            sys.exit()
    pygame.display.update()