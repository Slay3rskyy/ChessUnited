import pygame

def king(x, y, window, width):

	king_image = pygame.image.load("C:\\Users\\admin\\OneDrive\\Pulpit\\zabawa z pythonem\\CHESS UNITED\\king_image.png").convert()
	king_figure = pygame.transform.scale(king_image, (width // 12 , width // 12))

	window.blit(king_figure,(x,y))