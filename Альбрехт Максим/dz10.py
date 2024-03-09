import pygame
from pygame.locals import *
import time

pygame.init()
pygame.display.set_caption('Рисуем!')
screen = pygame.display.set_mode((800,600))

play = True
clock = pygame.time.Clock()
sky = Rect(0, 0, 800, 300)
ground = Rect(0, 300, 800, 300)

pygame.draw.rect(screen,(30,100,200), sky)
pygame.draw.rect(screen,(39,138,34), ground)

while play:
	for event in pygame.event.get():
		if event.type == QUIT:
			play = False
	pygame.display.update()
	clock.tick(60)