import pygame
import resources
import board


def king(x: int, y: int, window: pygame.display, width: int, ):
	KING_SIZE = (width // 9, width // 9)
	king_image = pygame.image.load(
		"resources/king_image.png").convert_alpha()
	king_figure = pygame.transform.scale(king_image, KING_SIZE)
	
	window.blit(king_figure, (x - KING_SIZE[0] // 2, y - KING_SIZE[1] // 2))
	if pygame.mouse.get_pressed()[0]:
		if ((pygame.mouse.get_pos()[0] >= (x - KING_SIZE[0] // 2)) and (
				pygame.mouse.get_pos()[0] <= (x + KING_SIZE[0] // 2))) and (
				pygame.mouse.get_pos()[1] >= (y - KING_SIZE[1] // 2)) and (
				pygame.mouse.get_pos()[1] <= (y + KING_SIZE[1] // 2)):
			print("it happened")
		# for i in board:
		# 	for j in board[i]:
		# 		try:
		# 			window.blit(king_figure)
		#
