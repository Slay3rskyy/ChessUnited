import pygame


def set_board(win, width, height):
	board = [[""]]
	
	chess_black = (30,30,30)
	chess_white = (205,205,205)
	
	for i in range(0, 8):
		board.append([])
		for j in range(0, 8):
			
			if (i + j) % 2 == 0:
				
				board[i].append("w")
				pygame.draw.rect(win, chess_white,
								 pygame.Rect(width // 8 * i, height // 8 * j, width // 8, height // 8))
			else:
				
				board[i].append("b")
				pygame.draw.rect(win, chess_black, pygame.Rect(width // 8 * i, height // 8 * j, width // 8, height // 8))


