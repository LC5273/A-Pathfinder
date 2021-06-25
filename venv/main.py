import pygame
import numpy as np
import time

# Initialising the pygame library
pygame.init()

# Creating the window
width = 900
heigth = 900
window = pygame.display.set_mode((width, heigth))
window_running = True

# Title and icon
pygame.display.set_caption("A* Pathfinding")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def fill(surface, color): # color = RGBA tuple
    w, h = surface.get_size()
    # r, g, b, a = color
    r, g, b = color
    for x in range(w):
        for y in range(h):
            # surface.set_at((x, y), pygame.Color(r, g, b, a))
            surface.set_at((x, y), pygame.Color(r, g, b))

def AlgorithmLee(matrix, startpoint, endpoint, sub, window):
    # Boardering the matrix
    matrix[0][0:] = -1
    matrix[rows + 1][0:] = -1
    for i in range(1, rows+1):
        matrix[i][0] = -1
        matrix[i][coloums + 1] = -1

    matrix[startpoint[1] + 1][startpoint[0] + 1] = 1
    # print(startpoint[0])
    # print(startpoint[1])

    # Lee's Algorithm
    p = pygame.Rect(0, 0, width / coloums - 2, heigth / rows - 2)
    k = True
    while k:
        k = False
        for i in range(1, rows+1):
            for j in range(1, coloums+1):
                if matrix[i][j] > 0:
                    if matrix[i-1][j] == 0:
                        matrix[i-1][j] = matrix[i][j] + 1
                        k = True
                    if matrix[i+1][j] == 0:
                        matrix[i+1][j] = matrix[i][j] + 1
                        k = True
                    if matrix[i][j-1] == 0:
                        matrix[i][j-1] = matrix[i][j] + 1
                        k = True
                    if matrix[i][j+1] == 0:
                        matrix[i][j+1] = matrix[i][j] + 1
                        k = True

                    if (i-1, j-1) != startpoint and (i-1, j-1) != endpoint:
                        sub[j - 1][i - 1].fill((5, 250, 10), p)
                        window.blit(sub[j-1][i-1], (heigth * (j-1) / rows, width * (i-1) / coloums))
                        pygame.display.update()
                    time.sleep(0.001)



    print(matrix)


# Input the matrix size
print("Input the number of rows and coloums:")
rows, coloums = map(int, input().split())

matrix = np.zeros(shape=(rows + 2, coloums + 2))
#p = np.zeros(shape = (rows, coloums))
#sub = np.zeros(shape = (rows, coloums))

p = []
sub = []
matrix1 = []
for i in range(0, rows):
    row=[]
    for j in range(0, coloums):
        row.append(0)
    p.append(row)
    sub.append(row)
    matrix1.append(row)

canvas = pygame.Surface((width, heigth))

for row in range(0, rows):
    for coloum in range(0, coloums):
        p[row][coloum] = pygame.Rect(0, 0, width / coloums, heigth / rows)
        sub[row][coloum] = canvas.subsurface(p[row][coloum])
        pygame.draw.line(sub[row][coloum], (255, 255, 255), (width * (coloum + 1) / coloums, heigth * row / rows), (width * (coloum + 1) / coloums, heigth * (row + 1) / rows), 5)
        pygame.draw.line(sub[row][coloum], (255, 255, 255), (width * coloum / coloums, heigth * (row + 1) / rows), (width * (coloum + 1) / coloums, heigth * (row + 1) / rows), 5)
        # print(width * (coloum + 1) / coloums, heigth * row / rows, width * (coloum + 1) / coloums, heigth * (row + 1) / rows)
        window.blit(sub[row][coloum], (width * coloum / coloums, heigth * row / rows))


p1 = pygame.Rect(0, 0, width / coloums - 2, heigth / rows - 2)
p2 = pygame.Rect(0, 0, width / coloums - 2, heigth / rows - 2)
p3 = pygame.Rect(0, 0, width / coloums - 2, heigth / rows - 2)
# p2 = pygame.Rect(0, 0, 200, 200)
#
# sub1 = canvas.subsurface(p1)
# sub2 = canvas.subsurface(p2)
#
# pygame.draw.line(sub1, (255, 255, 255), (200, 0), (200, 200), 5)
# pygame.draw.line(sub2, (255, 255, 255), (200, 0), (200, 200), 5)
#
# window.blit(sub1, (0, 0))
# window.blit(sub2, (200, 0))
# pygame.display.update()

# p[0][0].fill((255, 0, 0))
# pygame.draw.rect(window, (255, 0, 0), p[1][1])



# fill(sub[1][1], pygame.Color(255, 0, 0, 100))

# pygame.draw.rect(window, (255, 0, 0), p1)

# p[0][0] = pygame.Surface.fill((255, 0, 0))

# FILLING A subSURFACE
# sub[0][0].fill((255, 0, 0), p1)
# window.blit(sub[0][0], (0, 0))

pygame.display.update()

click = 0

while window_running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            window_running = False
        if event.type == pygame.MOUSEBUTTONUP and click == 0:
            click = 1
            pos = pygame.mouse.get_pos()
            # print(pos[0])
            start_row = int(pos[0] / (width / coloums))
            start_coloum = int(pos[1] / (heigth / rows))

            sub[start_row][start_coloum].fill((0, 0, 255), p1)
            window.blit(sub[start_row][start_coloum], (heigth * start_row / rows, width * start_coloum / coloums))

        elif event.type == pygame.MOUSEBUTTONUP and click == 1:
            pos = pygame.mouse.get_pos()
            # print(pos[0])
            print('ENDPOINT')
            end_row = int(pos[0] / (width / coloums))
            end_coloum = int(pos[1] / (heigth / rows))

            if start_row != end_row or start_coloum != end_coloum:
                click = 2
                matrix[end_coloum + 1][end_row + 1] = -1
                sub[end_row][end_coloum].fill((255, 0, 255), p2)
                window.blit(sub[end_row][end_coloum], (heigth * end_row / rows, width * end_coloum / coloums))

        elif event.type == pygame.MOUSEBUTTONUP and click == 2:
            pos = pygame.mouse.get_pos()
            obs_row = int(pos[0] / (width / coloums))
            obs_coloum = int(pos[1] / (heigth / rows))

            if (obs_row, obs_coloum) != (start_row, start_coloum) and (obs_row, obs_coloum) != (end_row, end_coloum):
                matrix[obs_coloum + 1, obs_row + 1] = -1
                sub[obs_coloum][obs_row].fill((255, 255, 255), p3)
                window.blit(sub[obs_coloum][obs_row], (heigth * obs_row / rows, width * obs_coloum / coloums))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and click == 2:
            click = 3
            AlgorithmLee(matrix, (start_row, start_coloum), (end_row, end_coloum), sub, window)


    # screen fill
    #window.fill((255, 0, 0))
    pygame.display.update()