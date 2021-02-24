import pygame
from pygame.locals import *


def printChart():
    pygame.draw.line(screen, (245, 245, 66), (250, 50), (250, 650), 3)
    pygame.draw.line(screen, (245, 245, 66), (450, 50), (450, 650), 3)
    pygame.draw.line(screen, (245, 245, 66), (50, 250), (650, 250), 3)
    pygame.draw.line(screen, (245, 245, 66), (50, 450), (650, 450), 3)


def printMouse(turn):
    mousePos = pygame.mouse.get_pos()
    if turn % 2 == 0:
        screen.blit(blueMouse, (mousePos[0], mousePos[1]))
    else:
        screen.blit(redMouse, (mousePos[0], mousePos[1]))


def printOX():
    for i in range(0, 9):
        if whoUsed[i] == 1:
            printX(getx(i), gety(i))
        elif whoUsed[i] == 2:
            printO(getx(i), gety(i))


def printX(x, y):
    pygame.draw.line(screen, (255, 0, 0), (x - 50, y - 50), (x + 50, y + 50), 2)
    pygame.draw.line(screen, (255, 0, 0), (x + 50, y - 50), (x - 50, y + 50), 2)


def printO(x, y):
    pygame.draw.circle(screen, (0, 42, 255), (x, y), 60, 2)


def setOX():
    mousePos = pygame.mouse.get_pos()
    if mousePos[0] < 250 and mousePos[1] < 250:
        return 0
    elif mousePos[0] > 250 and mousePos[0] < 450 and mousePos[1] < 250:
        return 1
    elif mousePos[0] > 450 and mousePos[1] < 250:
        return 2
    elif mousePos[0] < 250 and mousePos[1] > 250 and mousePos[1] < 450:
        return 3
    elif mousePos[0] > 250 and mousePos[0] < 450 and mousePos[1] > 250 and mousePos[1] < 450:
        return 4
    elif mousePos[0] > 450 and mousePos[1] > 250 and mousePos[1] < 450:
        return 5
    elif mousePos[0] < 250 and mousePos[1] > 450:
        return 6
    elif mousePos[0] > 250 and mousePos[0] < 450 and mousePos[1] > 450:
        return 7
    elif mousePos[0] > 450 and mousePos[1] > 450:
        return 8
    else:
        return 9


def noOX(posi):
    if whoUsed[posi] != 0:
        return 1
    else:
        return 0


def getx(posi):
    if posi == 0 or posi == 3 or posi == 6:
        return 150
    elif posi == 1 or posi == 4 or posi == 7:
        return 350
    elif posi == 2 or posi == 5 or posi == 8:
        return 550


def gety(posi):
    if posi >= 0 and posi <= 2:
        return 150
    elif posi >= 3 and posi <= 5:
        return 350
    elif posi >= 6 and posi <= 8:
        return 550


def checkWin():
    for i in range(0, 9, 3):
        if whoUsed[0+i] == whoUsed[1+i] and whoUsed[1+i] == whoUsed[2+i] and whoUsed[0+i] == 2:
            return 2
        elif whoUsed[0+i] == whoUsed[1+i] and whoUsed[1+i] == whoUsed[2+i] and whoUsed[0+i] == 1:
            return 1
    for j in range(0, 3):
        if whoUsed[0+j] == whoUsed[3+j] and whoUsed[3+j] == whoUsed[6+j] and whoUsed[0+j] == 2:
            return 2
        elif whoUsed[0+j] == whoUsed[3+j] and whoUsed[3+j] == whoUsed[6+j] and whoUsed[0+j] == 1:
            return 1
    if whoUsed[0] == whoUsed[4] and whoUsed[4] == whoUsed[8] and whoUsed[0] == 2:
        return 2
    elif whoUsed[0] == whoUsed[4] and whoUsed[4] == whoUsed[8] and whoUsed[0] == 1:
        return 1
    elif whoUsed[2] == whoUsed[4] and whoUsed[4] == whoUsed[6] and whoUsed[2] == 2:
        return 2
    elif whoUsed[2] == whoUsed[4] and whoUsed[4] == whoUsed[6] and whoUsed[2] == 1:
        return 1
    counter = 0
    for i in range(0, 9):
        if whoUsed[i] != 0:
            counter += 1
    if counter == 9:
        return 9


#Header
pygame.init()
screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption('TicTacToe')
pygame.mouse.set_visible(False)
pygame.font.init()
blueMouse = pygame.image.load('Graphics/blueCur.cur')
redMouse = pygame.image.load('Graphics/redCur.cur')

#Variables
running = True
turn = 0
stillUp = 0
win = 0
whoUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if win >= 1 and win <= 3:
                turn = 0
                win = 0
                stillUp = 0
                whoUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                pygame.mouse.set_visible(False)
    if win >= 1 and win <= 3:
        screen.fill((0, 0, 0))
        myFont = pygame.font.SysFont('Comic Sans MS', 20)
        textBlue = myFont.render('Blau hat gewonnen.', False, (0, 42, 255))
        textRed = myFont.render('Rot hat gewonnen.', False, (255, 0, 0))
        textDraw = myFont.render('Unentschieden.', False, (255, 255, 255))
        textAgain = myFont.render('Um nochmal zu spielen drücke eine beliebige Taste...', False, (255, 255, 255))
        if win == 2:
            printMouse(2)
            screen.blit(textBlue, (20, 20))
        elif win == 1:
            printMouse(1)
            screen.blit(textRed, (20, 20))
        elif win == 3:
            pygame.mouse.set_visible(True)
            screen.blit(textDraw, (20, 20))
        screen.blit(textAgain, (20, 80))
    else:
        if event.type == pygame.MOUSEBUTTONDOWN and stillUp == 0:
            stillUp = 1
            position = setOX()
            if position != 9:
                if noOX(position) == 0:
                    if turn % 2 == 0:
                        whoUsed[position] = 2
                    else:
                        whoUsed[position] = 1
                    turn += 1
        elif event.type == pygame.MOUSEBUTTONUP and stillUp == 1:
            stillUp = 0

        screen.fill((0, 0, 0))
        printMouse(turn)
        printChart()
        printOX()
        if checkWin() == 2:
            win = 2
        elif checkWin() == 1:
            win = 1
        elif checkWin() == 9:
            win = 3
    pygame.display.update()

pygame.quit()