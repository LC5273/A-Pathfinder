import pygame
import numpy as np

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

# Input the matrix size
print("Input the number of rows and coloums:")
rows, coloums = map(int, input().split())

matrix = np.zeros(shape = (rows, coloums))
#p = np.zeros(shape = (rows, coloums))
#sub = np.zeros(shape = (rows, coloums))

p = []
sub = []
for i in range(0, rows):
    row=[]
    for j in range(0, coloums):
        row.append(0)
    p.append(row)
    sub.append(row)

canvas = pygame.Surface((width, heigth))

for row in range(0, rows):
    for coloum in range(0, coloums):
        # p[row][coloum] = pygame.Rect(width * coloum / coloums, heigth * row / rows, width * (coloum + 1) / coloums, heigth * (row + 1) / rows)
        p[row][coloum] = pygame.Rect(0, 0, width / coloums, heigth / rows)
        sub[row][coloum] = canvas.subsurface(p[row][coloum])
        pygame.draw.line(sub[row][coloum], (255, 255, 255), (width * (coloum + 1) / coloums, heigth * row / rows), (width * (coloum + 1) / coloums, heigth * (row + 1) / rows), 5)
        pygame.draw.line(sub[row][coloum], (255, 255, 255), (width * coloum / coloums, heigth * (row + 1) / rows), (width * (coloum + 1) / coloums, heigth * (row + 1) / rows), 5)
        print(width * (coloum + 1) / coloums, heigth * row / rows, width * (coloum + 1) / coloums, heigth * (row + 1) / rows)
        window.blit(sub[row][coloum], (width * coloum / coloums, heigth * row / rows))


# p1 = pygame.Rect(0, 0, 200, 200)
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

pygame.display.update()

while window_running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            window_running = False

    # screen fill
    #window.fill((255, 0, 0))
    pygame.display.update()