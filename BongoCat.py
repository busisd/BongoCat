#Coded by Daniel Busis
#Inspired by (and art taken from) https://bongo.cat
#Bongo sounds from https://www.freesound.org
#Music from: https://www.bensound.com

import pygame
import random

class BongoCatGameController():
	def __init__(self):
		self.CAT_NONE_DOWN_FILE = "./images/BongoCatBothUp.png"
		self.CAT_LEFT_DOWN_FILE = "./images/BongoCatLeftDown.png"
		self.CAT_RIGHT_DOWN_FILE = "./images/BongoCatRightDown.png"
		self.CAT_BOTH_DOWN_FILE = "./images/BongoCatBothDown.png"
		self.CAT_NONE_DOWN_IMAGE = pygame.image.load(self.CAT_NONE_DOWN_FILE)
		self.CAT_LEFT_DOWN_IMAGE = pygame.image.load(self.CAT_LEFT_DOWN_FILE)
		self.CAT_RIGHT_DOWN_IMAGE = pygame.image.load(self.CAT_RIGHT_DOWN_FILE)
		self.CAT_BOTH_DOWN_IMAGE = pygame.image.load(self.CAT_BOTH_DOWN_FILE)

		self.BULB_FILE = "./images/bulb.png"
		self.DISCO_FILE = "./images/disco.png"
		self.RAINBOW_FILE = "./images/rainbow.png"
		self.BULB_IMAGE = pygame.image.load(self.BULB_FILE)
		self.DISCO_IMAGE = pygame.image.load(self.DISCO_FILE)
		self.RAINBOW_IMAGE = pygame.image.load(self.RAINBOW_FILE)
		
		self.CAT_NONE_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_LEFT_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_RIGHT_DOWN_IMAGE.set_colorkey((255,255,255))
		self.CAT_BOTH_DOWN_IMAGE.set_colorkey((255,255,255))

		self.BONGO_SOUND_LOW_FILE = "sounds/low_bongo.wav"
		self.BONGO_SOUND_HIGH_FILE = "sounds/high_bongo.wav"
		self.BONGO_SOUND_LOW = pygame.mixer.Sound(self.BONGO_SOUND_LOW_FILE)
		self.BONGO_SOUND_HIGH = pygame.mixer.Sound(self.BONGO_SOUND_HIGH_FILE)
		
		self.MUSIC_POP_FILE = "music/bensound-creativeminds.mp3"
		self.MUSIC_JAZZ_FILE = "music/bensound-jazzyfrenchy.mp3"
		self.MUSIC_TECH_FILE = "music/bensound-summer.mp3"
		self.MUSIC_JINGLE_FILE = "music/bensound-ukulele.mp3"
		self.cur_song = -1
		self.song_list = [self.MUSIC_POP_FILE, self.MUSIC_JAZZ_FILE, self.MUSIC_TECH_FILE, self.MUSIC_JINGLE_FILE]
		self.SONG_VOLUME = .45
		
		self.left_down = False
		self.right_down = False
		
		self.bg_color = pygame.Color(255,255,255)
		self.lightswitch_mode = False
		self.disco_mode = False
		
		self.screen = None
		self.game_clock = None
		
		self.rainbow = RainbowControl()
		self.rainbow_mode = False
		
class RainbowControl():
	def __init__(self):
		self.color_percents = [1.0,1.0,1.0]
		self.frames_per_shift = 60
		self.cur_frames = 0
		self.color_goals = None
		self.color_steps = None
		self._choose_new_color_goals()
		
	def get_color(self):
		return pygame.Color(int(self.color_percents[0]*255),int(self.color_percents[1]*255),int(self.color_percents[2]*255))
		print(self.color_percents)
		
	def shift_rainbow(self):
		self.cur_frames+=1
		for i in range(0,3):
			self.color_percents[i] += self.color_steps[i]
			if self.color_percents[i] < 0:
				self.color_percents[i] = 0
		
		if self.cur_frames >= self.frames_per_shift:
			self.cur_frames=0
			self._choose_new_color_goals()
		
	def _choose_new_color_goals(self):
		self.color_goals = [random.random(), random.random(), random.random()]
		self.color_steps = [(1.0/self.frames_per_shift)*(self.color_goals[i] - self.color_percents[i]) for i in range(0,3)]
		
def main():
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init()
	pygame.init()	
	
	game_control = BongoCatGameController()
	pygame.display.set_caption("BONGO CAT")
	game_control.screen = pygame.display.set_mode((800,450))
	
	game_control.game_clock = pygame.time.Clock()
	
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
				if event.key==100:
					game_control.disco_mode = not game_control.disco_mode
				if event.key==114:
					game_control.rainbow_mode = not game_control.rainbow_mode
				if event.key==119:
					_return_to_white(game_control)
				if event.key==276:
					_left_bongo_down(game_control)
				if event.key==275:
					_right_bongo_down(game_control)
				if event.key==273:
					_toggle_song(game_control, 1)
				if event.key==274:
					_toggle_song(game_control, -1)
			if event.type == pygame.KEYUP:
				if event.key==276:
					_left_bongo_up(game_control)
				if event.key==275:
					_right_bongo_up(game_control)
		if game_control.disco_mode:
			_randomize_colors(game_control)
		if game_control.rainbow_mode:
			game_control.rainbow.shift_rainbow()
			game_control.bg_color = game_control.rainbow.get_color()
			
		_update_screen(game_control)
		game_control.game_clock.tick(60)
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

def _randomize_colors(game_control):
	new_colors = []
	for color in [game_control.bg_color.r, game_control.bg_color.g, game_control.bg_color.b]:
		change_amount = random.randrange(-4,5)
		if color + change_amount <= 255 and color + change_amount >= 0:
			color += change_amount
		elif change_amount>0:
			color = 255
		else:
			color = 0
		new_colors.append(color)

	game_control.bg_color.r = new_colors[0]
	game_control.bg_color.g = new_colors[1]
	game_control.bg_color.b = new_colors[2]

def _return_to_white(game_control):
	game_control.bg_color= pygame.Color(255,255,255)
	
def _update_screen(game_control):
	game_control.screen.fill(game_control.bg_color)
	background_image = _choose_cat_image(game_control)
	game_control.screen.blit(background_image, (0,0))
	if game_control.rainbow_mode:
		game_control.screen.blit(game_control.RAINBOW_IMAGE, (20,450-64-20))		
	else:
		if game_control.lightswitch_mode:
			game_control.screen.blit(game_control.BULB_IMAGE, (20,450-64-20))
		if game_control.disco_mode:
			game_control.screen.blit(game_control.DISCO_IMAGE, (20+64,450-64-20))
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

def _toggle_song(game_control, toggle_direction):
	pygame.mixer.music.stop()
	game_control.cur_song += toggle_direction
	if game_control.cur_song >= len(game_control.song_list):
		game_control.cur_song -= len(game_control.song_list) + 1
	if game_control.cur_song < -1:
		game_control.cur_song += len(game_control.song_list)
	if not game_control.cur_song == -1:
		pygame.mixer.music.load(game_control.song_list[game_control.cur_song])
		pygame.mixer.music.set_volume(game_control.SONG_VOLUME)
		pygame.mixer.music.play()
		
if __name__=="__main__":
	main()