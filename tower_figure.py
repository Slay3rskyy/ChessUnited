import pygame
import resources

def tower(x, y, window, width):
	TOWER_SIZE = (width // 12, width // 12)
	tower_image = pygame.image.load(
		"resources/tower_image.png").convert_alpha()
	tower_figure = pygame.transform.scale(tower_image, TOWER_SIZE)

	window.blit(tower_figure, (x - TOWER_SIZE[0] // 2, y - TOWER_SIZE[1] // 2))