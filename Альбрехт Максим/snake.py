import pygame
from pygame.locals import *
from random import randint
import time

pygame.init()
pygame.display.set_caption("Змейка")
screen = pygame.display.set_mode((800,600))
play = True
clock = pygame.time.Clock()
head = Rect(400, 300, 30, 30)

def random_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	return(r, g, b)

SPEED = 2
COLOR = random_color()
DIRECTION = [SPEED, 0]


def move(head):
	global DIRECTION, COLOR
	if KEYS[K_UP]:
		DIRECTION = [0, -SPEED]
		COLOR = random_color()
	elif KEYS[K_DOWN]:
		DIRECTION = [0, SPEED]
		COLOR = random_color()
	elif KEYS[K_LEFT]:
		DIRECTION = [-SPEED, 0]
		COLOR = random_color()
	elif KEYS[K_RIGHT]:
		DIRECTION = [SPEED, 0]
		COLOR = random_color()
	
	if head.bottom > 600:
		DIRECTION = [0, -SPEED]
		COLOR = random_color()
	elif head.top < 0:
		DIRECTION = [0, SPEED]
		COLOR = random_color()
	elif head.left < 0:
		DIRECTION = [SPEED, 0]
		COLOR = random_color()
	elif head.right > 800:
		DIRECTION = [-SPEED, 0]
		COLOR = random_color()
	head.move_ip(DIRECTION)
while play:
	for event in pygame.event.get():
		if event.type == QUIT:
			play = False
	KEYS = pygame.key.get_pressed()
	pygame.draw.rect(screen, COLOR, head)
	move(head)
	pygame.display.update()
	clock.tick(60)
