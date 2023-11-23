import pygame
import resources

def king(x, y, window, width):
	KING_SIZE = (width // 6, width // 6)
	king_image = pygame.image.load(
		"resources/king_image.jpg").convert_alpha()
	king_figure = pygame.transform.scale(king_image, KING_SIZE)

	window.blit(king_figure, (x - KING_SIZE[0] // 2, y - KING_SIZE[1] // 2))
