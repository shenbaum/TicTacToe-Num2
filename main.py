import pygame, random
from var import *
import numpy

Win = pygame.display.set_mode((size))
pygame.display.set_caption('TicTacToe')

board = numpy.zeros((boardRows, boardCols))
text = font.render(('PLAYER(' + str(turn) + ') IS THE WINNER!'), True, lineColor)

def markSquare(row, col, player):
    board[row][col] = player

def availableSquare(row, col):
    return board[row][col] == 0

def drawFigures():
    for row in range(boardRows):
        for col in range(boardCols):
            if board[row][col] == 1:
                pygame.draw.circle(Win, white, (int(col * 200 + 100), int(row * 200 + 100)), circleRadius, circleWidth)
            elif board[row][col] == 2:
                pygame.draw.line(Win, white, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), crossWidth)
                pygame.draw.line(Win, white, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), crossWidth)

def boardIsFull():
    for row in range(boardRows):
        for col in range(boardCols):
            if board[row][col] == 0:
                return False

def checkWinner(turn):
    global playerOneIsWinner, playerTwoIsWinner

    for col in range(boardCols):
        if board[0][col] == turn and board[1][col] == turn and board[2][col] == turn:
            if turn == 1:
                playerOneIsWinner = True
            elif turn == 2:
                playerTwoIsWinner = True

    for row in range(boardRows):
        if board[row][0] == turn and board[row][1] == turn and board[row][2] == turn:
            if turn == 1:
                playerOneIsWinner = True
            elif turn == 2:
                playerTwoIsWinner = True

    if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        if turn == 1:
            playerOneIsWinner = True
        elif turn == 2:
            playerTwoIsWinner = True

    if board[2][0] == turn and board[1][1] == turn and board[0][2] == turn:
        if turn == 1:
            playerOneIsWinner = True
        elif turn == 2:
            playerTwoIsWinner = True       

def playerWon():
    Win.fill(backgroundColor)
    Win.blit(text, (37, 250))

def lines():
    # 1 horizontal
    pygame.draw.line(Win, lineColor, (0, 200), (600, 200), lineWidth)
    # 2 horizontal
    pygame.draw.line(Win, lineColor, (0, 400), (600, 400), lineWidth)
    # 1 vertical
    pygame.draw.line(Win, lineColor, (200, 0), (200, 600), lineWidth)
    # 2 vertical
    pygame.draw.line(Win, lineColor, (400, 0), (400, 600), lineWidth)

Win.fill(backgroundColor)
lines()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos[0], event.pos[1]
            clickedCol, clickedRow = int(mx // 200), int(my // 200)
            
            if availableSquare(clickedRow, clickedCol):
                if turn == 1:
                    markSquare(clickedRow, clickedCol, 1)

                elif turn == 2:
                    markSquare(clickedRow, clickedCol, 2)

                drawFigures()
                
                checkWinner(turn)
                if playerOneIsWinner or playerTwoIsWinner:
                    playerWon()

                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1

    pygame.display.update()

pygame.quit()
