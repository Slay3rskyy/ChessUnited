import pygame
import resources

def knight(x, y, window, width):
	KNIGHT_SIZE = (width // 12, width // 12)
	knight_image = pygame.image.load(
		"resources/knight_image.png").convert_alpha()
	knight_figure = pygame.transform.scale(knight_image, KNIGHT_SIZE)

	window.blit(knight_figure, (x - KNIGHT_SIZE[0] // 2, y - KNIGHT_SIZE[1] // 2))