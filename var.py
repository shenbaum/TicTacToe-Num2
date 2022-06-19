import pygame, random

pygame.init()

size = (600, 600)
backgroundColor = (28, 170, 156)

boardRows, boardCols = 3, 3

lineColor = (23, 145, 135)
lineWidth = 15

white = (255, 255, 255)
circleWidth = 15
circleRadius = 60

circleX, circleY = 300, 300

space = 55
crossWidth = 25

players = [1, 2]
turn = random.choice(players)
playerOneIsWinner, playerTwoIsWinner = False, False

font = pygame.font.Font('Vonique 64.ttf', 48)
