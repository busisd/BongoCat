import pygame

class BongoCatGameController():
	def __init__(self):
		self.CAT_NONE_DOWN_FILE = "BongoCatBothUp.png"
		self.CAT_LEFT_DOWN_FILE = "BongoCatLeftDown.png"
		self.CAT_RIGHT_DOWN_FILE = "BongoCatRightDown.png"
		self.CAT_BOTH_DOWN_FILE = "BongoCatBothDown.png"
		self.CAT_NONE_DOWN_IMAGE = pygame.image.load("images/BongoCatBothUp.png")
		self.CAT_LEFT_DOWN_IMAGE = pygame.image.load("images/BongoCatLeftDown.png")
		self.CAT_RIGHT_DOWN_IMAGE = pygame.image.load("images/BongoCatRightDown.png")
		self.CAT_BOTH_DOWN_IMAGE = pygame.image.load("images/BongoCatBothDown.png")
		
		self.left_down = False
		self.right_down = False
		
		self.screen = None
		
def main():
	
	
	
	game_control = BongoCatGameController()
	
	pygame.init()
	pygame.display.set_caption("BONGO CAT")
	game_control.screen = pygame.display.set_mode((800,450))
	
	running = True
	while(running):
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				running = False
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					game_control.left_down = True
				if event.button==3:
					game_control.right_down = True
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button==1:
					game_control.left_down = False
				if event.button==3:
					game_control.right_down = False

		_update_screen(game_control)
	pygame.quit()

def _update_screen(game_control):
	game_control.screen.fill(pygame.Color(255,255,255))
	background_image = _choose_cat_image(game_control)
	game_control.screen.blit(background_image, (0,0))
	pygame.display.update()
	
def _choose_cat_image(game_control):
	if game_control.left_down and game_control.right_down:
		return game_control.CAT_BOTH_DOWN_IMAGE
	elif game_control.left_down:
		return game_control.CAT_LEFT_DOWN_IMAGE
	elif game_control.right_down:
		return game_control.CAT_RIGHT_DOWN_IMAGE
	else:
		return game_control.CAT_NONE_DOWN_IMAGE
	
if __name__=="__main__":
	main()