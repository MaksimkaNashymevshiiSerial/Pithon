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
house = Rect(225,150,350,250)
windowz = Rect(350,60,100,60)
windowz2 = Rect(320,200,160,140)
palka = Rect(30,151,200,20)
palochka = Rect(30,151,200,250)
fondlyapalochek = Rect(60,170,200,230)
stvol = Rect(650,250,25,250)
stvol2 = Rect(90,300,25,250)

pygame.draw.rect(screen,(30,100,200), sky)
pygame.draw.rect(screen,(39,138,34), ground)
pygame.draw.rect(screen,(165, 42, 42), house)
pygame.draw.circle(screen,(255,255,0),(800,0),100)
pygame.draw.line(screen,(255,255,0),[800,0],[625,25],5)
pygame.draw.line(screen,(255,255,0),[800,0],[605,75],5)
pygame.draw.line(screen,(255,255,0),[800,0],[700,200],5)
pygame.draw.line(screen,(255,255,0),[800,0],[610,180],5)
pygame.draw.line(screen,(255,255,0),[800,0],[780,140],5)
pygame.draw.polygon(screen, (128, 0, 0), [[400,20], [200,150], [600,150]])
pygame.draw.ellipse(screen,(0, 0, 0), windowz)
pygame.draw.line(screen,(255,255,0),[350,90],[450,90],5)
pygame.draw.line(screen,(255,255,0),[400,60],[400,120],5)
pygame.draw.rect(screen,(247, 233, 230), windowz2)
pygame.draw.line(screen,(255,255,0),[400,340],[400,200],5)
pygame.draw.line(screen,(255,255,0),[320,270],[480,270],5)
pygame.draw.rect(screen,(165, 42, 42), palka)
pygame.draw.rect(screen,(165, 42, 42), palochka)
pygame.draw.rect(screen,(82, 31, 14), fondlyapalochek)
pygame.draw.polygon(screen, (128, 0, 0), [[200,20], [30,150], [300,150]])
pygame.draw.rect(screen,(165, 42, 42), stvol)
pygame.draw.line(screen,(165, 42, 42),[650,350],[600,270],5)
pygame.draw.line(screen,(165, 42, 42),[670,350],[715,270],5)
pygame.draw.circle(screen,(0,153,92),(660,200),100)
pygame.draw.rect(screen,(165, 42, 42), stvol2)
pygame.draw.line(screen,(165, 42, 42),[110,370],[160,270],5)
pygame.draw.line(screen,(165, 42, 42),[90,370],[50,270],5)
pygame.draw.circle(screen,(0,153,92),(100,220),100)

while play:
	for event in pygame.event.get():
		if event.type == QUIT:
			play = False
	pygame.display.update()
	clock.tick(60)