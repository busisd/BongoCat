#class BackgroundSprite(pygame.sprite.Sprite):
#	def __init__(self, image_file_path, top_left_corner):
#        pygame.sprite.Sprite.__init__(self)
#		self.image = pygame.image.load("BongoCatBothUp.png")
		

import pygame
#def main():
CAT_BOTH_UP_FILE = "BongoCatBothUp.png"

pygame.init()
pygame.display.set_caption("BONGO CAT")
screen = pygame.display.set_mode((800,450))
screen.fill(pygame.Color(255,255,255))
pygame.display.update()

running = True

while(running):
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			running = False
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				screen.fill(pygame.Color(0,255,0))
				pygame.display.update()
		if event.type == pygame.MOUSEBUTTONUP:
			screen.fill(pygame.Color(255,255,255))
			pygame.display.update()

pygame.quit()


#main()