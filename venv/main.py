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

def fill(surface, color): # color = RGBA tuple
    w, h = surface.get_size()
    # r, g, b, a = color
    r, g, b = color
    for x in range(w):
        for y in range(h):
            # surface.set_at((x, y), pygame.Color(r, g, b, a))
            surface.set_at((x, y), pygame.Color(r, g, b))

# def startPoint():


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


p1 = pygame.Rect(0, 0, width / coloums - 2, heigth / rows - 2)
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
print(p[0][0])
print(p1)
print(sub[0][0])

# fill(sub[1][1], pygame.Color(255, 0, 0, 100))

# pygame.draw.rect(window, (255, 0, 0), p1)

# p[0][0] = pygame.Surface.fill((255, 0, 0))

# FILLING A subSURFACE
sub[0][0].fill((255, 0, 0), p1)
window.blit(sub[0][0], (0, 0))

pygame.display.update()

click = 0

while window_running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            window_running = False
        # if event.type == pygame.mouse

    # screen fill
    #window.fill((255, 0, 0))
    pygame.display.update()