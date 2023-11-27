from pygame.locals import *
import pygame, sys, random

import board
import king_figure, queen_figure, rook_figure, knight_figure, bishop_figure
import pawn_script

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
fpsClock = pygame.time.Clock()


# The main function that controls the game
def main(width, height, fps):
    looping = True

    WINDOW = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game!')
    # The main game loop
    while looping:
        # Get inputs

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later
        # Render elements of the game

        WINDOW.fill(BACKGROUND)

        board.set_board(WINDOW, width, height)
        king_figure.king(board.figure_locations["D1"][0], board.figure_locations["D1"][1], WINDOW, width)
        queen_figure.queen(board.figure_locations["E1"][0], board.figure_locations["E1"][1], WINDOW, width)
        rook_figure.rook(board.figure_locations["A1"][0], board.figure_locations["A1"][1], WINDOW, width)
        rook_figure.rook(board.figure_locations["H1"][0], board.figure_locations["H1"][1], WINDOW, width)
        knight_figure.knight(board.figure_locations["B1"][0], board.figure_locations["B1"][1], WINDOW, width)
        knight_figure.knight(board.figure_locations["G1"][0], board.figure_locations["G1"][1], WINDOW, width)
        bishop_figure.bishop(board.figure_locations["C1"][0], board.figure_locations["C1"][1], WINDOW, width)
        bishop_figure.bishop(board.figure_locations["F1"][0], board.figure_locations["F1"][1], WINDOW, width)
        print(board.figure_locations)

        pygame.display.update()
        fpsClock.tick(fps)
