import pygame


def set_board(win, width, height):
	board = [[""]]
	
	for i in range(0, 8):
		board.append([])
		for j in range(0, 8):
			
			if (i + j) % 2 == 0:
				
				board[i].append("w")
				pygame.draw.rect(win, (255, 255, 255), pygame.Rect(width // 8 * i, height // 8 * j, width // 8, height // 8))
			else:
				
				board[i].append("b")
				pygame.draw.rect(win, (0, 0, 0), pygame.Rect(width // 8 * i, height // 8 * j, width // 8, height // 8))