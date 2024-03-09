import pygame as pg
from pygame.locals import *

class Block(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.block_width = 75
		self.block_height = 50
		self.size = [self.block_width, self.block_height]
		self.image = pg.Surface(self.size)
		self.image.fill((255,255,0))
		self.rect = self.image.get_rect()
		self.name = "BLOCK"
		self.health = 0


class Ball(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((15,15))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect(center=(400,500))
		self.ball_speed = 2
		self.score = 0
		self.is_moving = True
		self.speedx = self.ball_speed
		self.speedy = self.ball_speed * -1
		self.point = pg.mixer.Sound("score.mp3")
		self.bonus = pg.mixer.Sound("bonus2.mp3")
		self.bonce = pg.mixer.Sound("udar.mp3")

	def update(self, keys, platform, blocks, *args):
		if self.is_moving:
			self.rect.y += self.speedy
			hitGroup = pg.sprite.Group(platform, blocks)
			spriteHitList = pg.sprite.spritecollide(self, hitGroup, False)

			if len(spriteHitList) > 0:
				for sprite in spriteHitList:
					if sprite.name == "BLOCK":
						sprite.health -= 1
						if sprite.health == 0:
							sprite.kill()
						self.speedy *= -1
						self.score += 1
						if self.score % 10 == 0:
							self.bonus.play()
						else:
							self.point.play()
						self.rect.y += self.speedy
					elif sprite.name == "PLATFORM":
						self.speedy *= -1
						self.rect.y += self.speedy

			self.rect.x += self.speedx

			if self.rect.right > 800:
				self.speedx *= -1
				self.rect.right = 800
				self.bonce.play()

			if self.rect.left < 0:
				self.speedx *= -1
				self.rect.left = 0
				self.bonce.play()

			if self.rect.top < 0:
				self.speedy *= -1
				self.rect.top = 0	
			if self.rect.bottom > 600:
				self.is_moving = False
				self.speedx = self.ball_speed
				self.speedy = self.ball_speed * -1
				self.bonce.play()

class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((90, 10))
		self.rect = self.image.get_rect(center=(400, 590))
		self.image.fill((255,0,0))
		self.name = 'PLATFORM'

	def update(self, keys, *args):
		if keys[K_a] and self.rect.x >0:
			self.rect.x -= 15
		if keys[K_d] and self.rect.x < 740:
			self.rect.x += 15




class Game:
	def __init__(self):
		self.score = 0
		self.game_over = 0
		self.sprites = pg.sprite.Group()
		self.platform = Platform()
		self.sprites.add(self.platform)
		self.ball = Ball()
		self.sprites.add(self.ball)
		self.blocks = pg.sprite.Group()
		self.font = pg.font.Font(None, 32)

		for row in range(5):
			for col in range(10):
				block = Block()
				block.rect.x = col * (block.block_width + 7)
				block.rect.y = row * (block.block_height + 7)
				block.health = 5 - row
				self.blocks.add(block)
			self.sprites.add(self.blocks)

	def process_events(self):
		for event in pg.event.get():
			if event.type == QUIT:
				return True
			if event.type == MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()
					
	def run_logic(self):
		pass

	def display_frame(self, screen, keys):
		screen.fill((0,0,0))
		score = self.font.render('Score: ' + str(self.ball.score), 1, (255, 0, 0))
		screen.blit(score, [20, 550])
		self.sprites.update(keys, self.platform, self.blocks)
		self.sprites.draw(screen)

		if self.ball.is_moving == False:
			self.__init__()

def main():
	pg.init()
	pg.display.set_caption("Arcanoid")
	screen = pg.display.set_mode((800,600))
	endgame = False
	clock = pg.time.Clock()
	game = Game()

	while not endgame:
		endgame = game.process_events()
		game.run_logic()
		keys = pg.key.get_pressed()
		game.display_frame(screen, keys)
		pg.display.update()
		clock.tick(60)

if __name__ == "__main__":
	main()

