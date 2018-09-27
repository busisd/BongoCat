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
		
		self.CAT_NONE_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_LEFT_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_RIGHT_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_BOTH_DOWN_IMAGE.set_colorkey((255,255,255))

		self.BONGO_SOUND_LOW_FILE = "sounds/low_bongo.wav"
		self.BONGO_SOUND_HIGH_FILE = "sounds/high_bongo.wav"
		self.BONGO_SOUND_LOW = pygame.mixer.Sound(self.BONGO_SOUND_LOW_FILE)
		self.BONGO_SOUND_HIGH = pygame.mixer.Sound(self.BONGO_SOUND_HIGH_FILE)
		
		self.left_down = False
		self.right_down = False
		
		self.bg_color = pygame.Color(255,255,255)
		self.lightswitch_mode = False
		
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
			if event.type == pygame.QUIT:
				running = False
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					_left_bongo_down(game_control)
				if event.button==3:
					_right_bongo_down(game_control)
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button==1:
					_left_bongo_up(game_control)
				if event.button==3:
					_right_bongo_up(game_control)
			if event.type == pygame.KEYDOWN:
				if event.key==32:
					game_control.lightswitch_mode = not game_control.lightswitch_mode
				if event.key==276:
					_left_bongo_down(game_control)
				if event.key==275:
					_right_bongo_down(game_control)
			if event.type == pygame.KEYUP:
				if event.key==276:
					_left_bongo_up(game_control)
				if event.key==275:
					_right_bongo_up(game_control)

		_update_screen(game_control)
	pygame.quit()

def _left_bongo_down(game_control):
	game_control.left_down = True
	game_control.BONGO_SOUND_LOW.play()
	if game_control.lightswitch_mode:
		_brighten_bg(game_control, -15)

def _right_bongo_down(game_control):
	game_control.right_down = True
	game_control.BONGO_SOUND_HIGH.play()
	if game_control.lightswitch_mode:
		_brighten_bg(game_control, 15)

def _left_bongo_up(game_control):
	game_control.left_down = False

def _right_bongo_up(game_control):
	game_control.right_down = False
		
def _brighten_bg(game_control, brighten_amount):
	new_colors = []
	for color in [game_control.bg_color.r, game_control.bg_color.g, game_control.bg_color.b]:
		if color + brighten_amount <= 255 and color + brighten_amount >= 0:
			color += brighten_amount
		elif brighten_amount>0:
			color = 255
		else:
			color = 0
		new_colors.append(color)

	game_control.bg_color.r = new_colors[0]
	game_control.bg_color.g = new_colors[1]
	game_control.bg_color.b = new_colors[2]
	
def _update_screen(game_control):
	game_control.screen.fill(game_control.bg_color)
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