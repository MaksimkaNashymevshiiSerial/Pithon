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
font = pygame.font.Font('OceanwidePrimer-Semibold.otf', 32)

pygame.mixer.init()
game_sound = pygame.mixer.Sound("fon.wav")
game_sound.set_volume(0.4)
point_sound = pygame.mixer.Sound("points.wav")
game_sound.set_volume(0.8)

def load_image(src, x, y):
	image = pygame.image.load(src).convert()
	image = pygame.transform.scale(image,(30, 30))
	rect = image.get_rect(center = (x,y))
	transparent = image.get_at((0,0))
	image.set_colorkey(transparent)
	return image, rect
def random_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	return(r, g, b)

SPEED = 30
COLOR = random_color()
DIRECTION = [SPEED, 0]
GAME_POINTS = 0

def pickup():
	global apple_rect, head_rect, GAME_POINTS, snake

	if head_rect.colliderect(apple_rect):
		apple_rect.x = randint(40, 760)
		apple_rect.y = randint(40, 560)
		GAME_POINTS += 1
		print(f'Game poits: {GAME_POINTS}')
		snake.append(snake[-1].copy())
		point_sound.play()
	score()


def score():
	global GAME_POINTS
	text = font.render(f'Game poits: {GAME_POINTS}', True, (255,255,0))
	text_rect = text.get_rect(center=(400,500))
	screen.blit(text, text_rect)

def gameover():
	global snake, head_rect
	for segment in snake[1:]:
		if head_rect.colliderect(segment):
			return True
	return False

def move(head, snake):
	global DIRECTION, COLOR

	if KEYS[K_UP] and DIRECTION[1]==0:
		DIRECTION = [0, -SPEED]
	elif KEYS[K_DOWN] and DIRECTION[1]==0:
		DIRECTION = [0, SPEED]		
	elif KEYS[K_LEFT] and DIRECTION[0]==0:
		DIRECTION = [-SPEED, 0]		
	elif KEYS[K_RIGHT] and DIRECTION[0]==0:
		DIRECTION = [SPEED, 0]
	
	if head.bottom > 600:
		head.top = 0
	elif head.top < 0:
		head.bottom = 600
	elif head.left < 0:
		head.right = 800
	elif head.right > 800:
		head.left = 0
	#print(snake)
	for index in range(len(snake)-1, 0, -1):
		snake[index].x = snake[index-1].x
		snake[index].y = snake[index-1].y

	head.move_ip(DIRECTION)

head_image, head_rect = load_image("head.png", 400, 300)
apple_image, apple_rect = load_image("apple.png", 200, 300)
body_image, body_rect = load_image("body.png", 370, 300)

snake = [head_rect, body_rect]
game_sound.play()

while play:
	for event in pygame.event.get():
		if event.type == QUIT:
			play = False
	screen.fill((0,0,0))
	KEYS = pygame.key.get_pressed()
	screen.blit(head_image, head_rect)
	screen.blit(apple_image, apple_rect)
	for segment in snake[1:]:
		screen.blit(body_image, segment)

	#pygame.draw.rect(screen, COLOR, head)
	move(head_rect, snake)
	pickup()

	if gameover():
		play = False

	pygame.display.update()
	clock.tick(8)
