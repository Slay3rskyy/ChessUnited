import pygame
import resources

def queen(x, y, window, width):
	QUEEN_SIZE = (width // 12, width // 12)
	queen_image = pygame.image.load(
		"resources/queen_image.png").convert_alpha()
	queen_figure = pygame.transform.scale(queen_image, QUEEN_SIZE)

	window.blit(queen_figure, (x - QUEEN_SIZE[0] // 2, y - QUEEN_SIZE[1] // 2))