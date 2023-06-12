import pygame
import random

pygame.init()

win = pygame.display.set_mode((665, 500))

pygame.display.set_caption("Selection sort")

programIcon = pygame.image.load("selection.png")

pygame.display.set_icon(programIcon)

cant_rect = 20
x = 30
y = 30
width = 25
run = True
height = []

for k in range(cant_rect):
    height.append(random.randint(10, 200) * 2)


def setup_array(h):
    for c in range(cant_rect):
        h[c] = random.randint(10, 200) * 2


def show(h):
    for m in range(len(h)):
        pygame.draw.rect(win, (200, 150, 0), (x + 30 * m, y, width, h[m]))


def color(h):
    for f in range(len(h)):
        pygame.draw.rect(win, (0, 250, 50), (x + 30 * f, y, width, h[f]))

    pygame.display.update()


def array_sorted(arr):
    n = len(arr)

    if n == 1 or n == 0:
        return True

    return arr[0] <= arr[1] and array_sorted(arr[1:])


while run:

    execute = False

    pygame.time.delay(5)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        execute = True

    if not execute:

        win.fill((0, 0, 0))

        if not array_sorted(height):
            show(height)
        else:
            win.fill((0, 0, 0))
            color(height)
            pygame.time.delay(1000)
            setup_array(height)

        pygame.display.update()

    elif not array_sorted(height) and execute:

        for step in range(cant_rect):
            min_idx = step

            for i in range(step + 1, cant_rect):

                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if height[i] < height[min_idx]:
                    min_idx = i

            (height[step], height[min_idx]) = (height[min_idx], height[step])

            win.fill((0, 0, 0))

            show(height)

            pygame.time.delay(100)

            pygame.display.update()
        win.fill((0, 0, 0))
        color(height)
        pygame.time.delay(1000)
        setup_array(height)
        pygame.display.update()

pygame.quit()
