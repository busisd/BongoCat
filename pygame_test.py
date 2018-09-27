import pygame

class BongoCatGameController():
	def __init__(self):
		self.CAT_NONE_DOWN_FILE = "images/BongoCatBothUp.png"
		self.CAT_LEFT_DOWN_FILE = "images/BongoCatLeftDown.png"
		self.CAT_RIGHT_DOWN_FILE = "images/BongoCatRightDown.png"
		self.CAT_BOTH_DOWN_FILE = "images/BongoCatBothDown.png"
		self.CAT_NONE_DOWN_IMAGE = pygame.image.load(self.CAT_NONE_DOWN_FILE)
		self.CAT_LEFT_DOWN_IMAGE = pygame.image.load(self.CAT_LEFT_DOWN_FILE)
		self.CAT_RIGHT_DOWN_IMAGE = pygame.image.load(self.CAT_RIGHT_DOWN_FILE)
		self.CAT_BOTH_DOWN_IMAGE = pygame.image.load(self.CAT_BOTH_DOWN_FILE)
		
		self.BONGO_SOUND_LOW_FILE = "sounds/low_bongo.wav"
		self.BONGO_SOUND_HIGH_FILE = "sounds/high_bongo.wav"
		self.BONGO_SOUND_LOW = pygame.mixer.Sound(self.BONGO_SOUND_LOW_FILE)
		self.BONGO_SOUND_HIGH = pygame.mixer.Sound(self.BONGO_SOUND_HIGH_FILE)
		
		self.left_down = False
		self.right_down = False
		
		self.screen = None
		
def main():
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init()
	pygame.init()	
	
	game_control = BongoCatGameController()
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
					game_control.BONGO_SOUND_LOW.play()
				if event.button==3:
					game_control.right_down = True
					game_control.BONGO_SOUND_HIGH.play()
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