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
			if "8" not in x:
				pygame.draw.circle(window, board.p_color, (board.figure_locations[x[0] + str(int(x[1]) + 1)][0],
														board.figure_locations[x[0] + str(int(x[1]) + 1)][1]), 5, 5)
			if "1" not in x:
				pygame.draw.circle(window, board.p_color, (board.figure_locations[x[0] + str(int(x[1]) - 1)][0],
													   board.figure_locations[x[0] + str(int(x[1]) - 1)][1]), 5, 5)
			if "A" not in x:
				pygame.draw.circle(window, board.p_color,(board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + x[1]][0],
														   board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + x[1]][1]), 5, 5)
			if "H" not in x:
				pygame.draw.circle(window, board.p_color,(board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + x[1]][0],
														board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + x[1]][1]), 5,5)
			if "A" not in x and "8" not in x:
				pygame.draw.circle(window, board.p_color,
								   (board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + str(int(x[1]) + 1)][0],
									board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + str(int(x[1]) + 1)][1]), 5,
								   5)
			if "H" not in x and "8" not in x:
				pygame.draw.circle(window, board.p_color,
								   (board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + str(int(x[1]) + 1)][0],
									board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + str(int(x[1]) + 1)][1]), 5,
								   5)
			if "A" not in x and "1" not in x:
				pygame.draw.circle(window, board.p_color,
								   (board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + str(int(x[1]) - 1)][0],
									board.figure_locations[board.letters[board.letters.index(x[0]) - 1] + str(int(x[1]) - 1)][1]), 5,
								   5)
			if "H" not in x and "1" not in x:
				pygame.draw.circle(window, board.p_color,
								   (board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + str(int(x[1]) - 1)][0],
									board.figure_locations[board.letters[board.letters.index(x[0]) + 1] + str(int(x[1]) - 1)][1]), 5,
								   5)
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
		if not ((base_fig_location[0] >= mouse[0]-KING_SIZE[0]//2 and base_fig_location[1] >= mouse[1]-KING_SIZE[1]//2) and (base_fig_location[0] <= mouse[0]+ KING_SIZE[0]//2  and base_fig_location[1] <= mouse[1]+KING_SIZE[1]//2)):
			king_showing = False
		else:
			king_showing = True
		if king_showing:
			window.blit(king_fig, (mouse[0] - KING_SIZE[0] // 2, mouse[1] - KING_SIZE[1] // 2))