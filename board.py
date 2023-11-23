import pygame

import pawn_script


def set_board(win, width, height):
    board = [[""]]
    NOTATION_CONST = 25
    letters = "ABCDEFGH"

    global figure_locations
    figure_locations = {}

    chess_black = (30, 30, 30)
    chess_white = (205, 205, 205)
    notation_color = (127, 127, 127)
    nt = width // NOTATION_CONST + width % NOTATION_CONST  # notation width
    font = pygame.font.SysFont('timesnewroman', width // 25)
    font_color = (30, 30, 30)
    wb = (width - nt)  # width of board
    pawn_script.start_pos(win, (2, 2), board)
    for i in range(0, 8):
        board.append([])
        for j in range(0, 8):
            figure_locations[str(f"{letters[i]}{j + 1}")] = (
                (wb) // 8 * (i + 1) + nt - wb // 16, (wb) // 8 * (8 - j) - wb // 16)

            if (i + j) % 2 == 0:

                board[i].append("w")

                if i == 0:
                    pygame.draw.rect(win, notation_color,
                                     pygame.Rect(0, wb // 8 * j, nt, wb // 8))

                if j == 7:
                    pygame.draw.rect(win, notation_color,
                                     pygame.Rect(wb // 8 * i + nt, wb, wb // 8, nt))

                pygame.draw.rect(win, chess_white,
                                 pygame.Rect(wb // 8 * i + nt, wb // 8 * j, wb // 8,
                                             wb // 8))
            else:

                board[i].append("b")

                if i == 0:
                    pygame.draw.rect(win, notation_color,
                                     pygame.Rect(0, wb // 8 * j, nt, wb // 8))

                if j == 7:
                    pygame.draw.rect(win, notation_color,
                                     pygame.Rect(wb // 8 * i + nt, wb, wb // 8, nt))

                pygame.draw.rect(win, chess_black,
                                 pygame.Rect(wb // 8 * i + nt, wb // 8 * j, wb // 8,
                                             wb // 8))

            win.blit(font.render(str(8 - i), 1, font_color), (nt / 4, wb // 8 * i + wb // 24))
            win.blit(font.render(letters[i], 1, font_color),
                     (wb // 8 * i + wb // 24 + nt, wb))

            pygame.draw.rect(win, chess_black,
                             pygame.Rect(0, wb // 8 * i + wb // 8 - wb // 160, nt,
                                         wb // 80))
            pygame.draw.rect(win, chess_black,
                             pygame.Rect(wb // 8 * i + (nt - wb // 160), wb,
                                         wb // 80, nt))

    # DOKOŃCZYĆ
