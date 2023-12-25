import pygame
import resources
import board


def king(x: int, y: int, window: pygame.display, width: int):
	KING_SIZE = (width // 9, width // 9)
	king_image = pygame.image.load(
		"resources/king_image.png").convert_alpha()
	king_figure = pygame.transform.scale(king_image, KING_SIZE)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	window.blit(king_figure, (board.figure_locations[x][0] - KING_SIZE[0] // 2, board.figure_locations[x][1] - KING_SIZE[1] // 2))
	king_move(x, y, window, width, king_figure, board.figure_locations[x])
	if click[0]:
		if ((mouse[0] >= (board.figure_locations[x][0] - KING_SIZE[0] // 2)) and (
				mouse[0] <= (board.figure_locations[x][0] + KING_SIZE[0] // 2))) and (
				mouse[1] >= (board.figure_locations[x][1] - KING_SIZE[1] // 2)) and (
				mouse[1] <= (board.figure_locations[x][1] + KING_SIZE[1] // 2)):
			circles(x, window)
		# for i in board:
		# 	for j in board[i]:
		# 		try:
		# 			window.blit(king_figure)
		#

def king_move(x: int, y: int,window: pygame.display, width: int,king_fig:pygame.surface.Surface,base_fig_location:[int]):
	KING_SIZE = (width // 9, width // 9)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()[0]
	if click:
		king_showing = bool
		if not ((base_fig_location[0] >= mouse[0]-KING_SIZE[0]//2 and base_fig_location[1] >= mouse[1]-KING_SIZE[1]//2) and
				(base_fig_location[0] <= mouse[0]+ KING_SIZE[0]//2  and base_fig_location[1] <= mouse[1]+KING_SIZE[1]//2)):
			king_showing = False
		else:
			king_showing = True
		if king_showing:
			window.blit(king_fig, (mouse[0] - KING_SIZE[0] // 2, mouse[1] - KING_SIZE[1] // 2))

def circles(x, window):
	for i in range(0, 3):
		for k in range(0, 3):
			if i != 1 or k != 1:
				try:
					pygame.draw.circle(window, board.p_color,
					(board.figure_locations[board.letters[board.letters.index(x[0]) - 1 + i] + str(int(x[1]) - 1 + k)][0],
							board.figure_locations[board.letters[board.letters.index(x[0]) - 1 + i] + str(int(x[1]) - 1 + k)][1]),
							5,5)
				except: pass