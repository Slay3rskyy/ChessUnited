import pygame
import resources

def bishop(x, y, window, width):
	BISHOP_SIZE = (width // 12, width // 12)
	bishop_image = pygame.image.load(
		"resources/bishop_image.png").convert_alpha()
	bishop_figure = pygame.transform.scale(bishop_image, BISHOP_SIZE)

	window.blit(bishop_figure, (x - BISHOP_SIZE[0] // 2, y - BISHOP_SIZE[1] // 2))