from pygame.locals import *
import pygame, sys, random

import board
import king_figure
import pawn_script

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
fpsClock = pygame.time.Clock()


# The main function that controls the game
def main(width, height, fps):
	looping = True
	
	WINDOW = pygame.display.set_mode((width, height))
	pygame.display.set_caption('My Game!')
	# The main game loop
	while looping:
		# Get inputs
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		# Processing
		# This section will be built out later
		# Render elements of the game
		
		WINDOW.fill(BACKGROUND)
		
		board.set_board(WINDOW, width, height)
		king_figure.king(board.figure_locations["D1"][0], board.figure_locations["D1"][1], WINDOW, width)
		# print(board.figure_locations)
		
		pygame.display.update()
		fpsClock.tick(fps)
