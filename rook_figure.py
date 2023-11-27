import pygame
import resources

def rook(x, y, window, width):
	ROOK_SIZE = (width // 12, width // 12)
	rook_image = pygame.image.load(
		"resources/rook_image.png").convert_alpha()
	rook_figure = pygame.transform.scale(rook_image, ROOK_SIZE)

	window.blit(rook_figure, (x - ROOK_SIZE[0] // 2, y - ROOK_SIZE[1] // 2))