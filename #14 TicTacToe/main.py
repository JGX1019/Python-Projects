import pygame as pg
import sys
import time
from pygame.locals import *

pg.init()

import pygame as pg

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]
player = 1  
game_over = False

def draw_lines():
    
    pg.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)
    
    pg.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)

def draw_figures():
    
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1: 
                pg.draw.circle(screen, CIRCLE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), 
                               CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:  
                pg.draw.line(screen, CROSS_COLOR,
                             (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + SPACE),
                             (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE),
                             CROSS_WIDTH)
                pg.draw.line(screen, CROSS_COLOR,
                             (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + HEIGHT // 3 - SPACE),
                             (col * WIDTH // 3 + WIDTH // 3 - SPACE, row * HEIGHT // 3 + SPACE),
                             CROSS_WIDTH)
                
def check_winner():
    for col in range(BOARD_COLS):
        if board[0][col] != 0 and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            draw_vertical_winning_line(col)
            return board[0][col]

    for row in range(BOARD_ROWS):
        if board[row][0] != 0 and board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            draw_horizontal_winning_line(row)
            return board[row][0]

    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        draw_desc_diagonal() 
        return board[0][0]

    if board[2][0] != 0 and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        draw_asc_diagonal() 
        return board[2][0]
    return 0



def draw_vertical_winning_line(col):
    x_pos = col * WIDTH // 3 + WIDTH // 6
    pg.draw.line(screen, (0, 255, 0), (x_pos, 15), (x_pos, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(row):
    y_pos = row * HEIGHT // 3 + HEIGHT // 6
    pg.draw.line(screen, (0, 255, 0), (15, y_pos), (WIDTH - 15, y_pos), LINE_WIDTH)


def draw_asc_diagonal():
    pg.draw.line(screen, (0, 255, 0), (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)


def draw_desc_diagonal():
    pg.draw.line(screen, (0, 255, 0), (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)


def restart_game():
    screen.fill(WHITE)
    draw_lines()
    global board, player, game_over
    board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False


draw_lines()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] 
            mouseY = event.pos[1]  

            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_winner() != 0:
                    game_over = True
                player = 3 - player 

                draw_figures()

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                restart_game()

    pg.display.update()
