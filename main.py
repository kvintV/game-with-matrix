import pygame
import numpy as np
import random
import time
import requests
import io


def fill(r, g, b):
    window.fill((r, g, b))
    for a in range(height):
        for b in range(0, width, sq):
            pygame.draw.rect(window, (123, 123, 123), (b, a, 1, 1))
    for a in range(width):
        for b in range(0, height, sq):
            pygame.draw.rect(window, (123, 123, 123), (a, b, 1, 1))


pygame.init()
width = 1200
height = 700
font = pygame.font.SysFont("Arial", 20)
window = pygame.display.set_mode((width, height))
run = True
screen = pygame.display.set_mode((width, height))
sq = 25
w = width // sq
h = height // sq
matrix = np.zeros((w, h))
'''16 12'''
fill(255,255, 255)
pygame.display.flip()
founded = []

while run:
    for i in range(w):
        for j in range(h):
            if matrix[i][j] == 2:
                if i != 0:
                    if matrix[i - 1][j] == 1:
                        matrix[i - 1][j] = 2
                        pygame.draw.rect(window, (255, 0, 0), ((i - 1) * sq + 1, j * sq + 1, sq - 1, sq - 1))
                if j != 0:
                    if matrix[i][j - 1] == 1:
                        matrix[i][j - 1] = 2
                        pygame.draw.rect(window, (255, 0, 0), (i * sq + 1, (j - 1) * sq + 1, sq - 1, sq - 1))
                if i != w - 1:
                    if matrix[i + 1][j] == 1:
                        pygame.draw.rect(window, (255, 0, 0), ((i + 1) * sq + 1, j * sq + 1, sq - 1, sq - 1))
                        founded.append((i + 1, j))
                if j != h - 1:
                    if matrix[i][j + 1] == 1:
                        pygame.draw.rect(window, (255, 0, 0), (i * sq + 1, (j + 1) * sq + 1, sq - 1, sq - 1))
                        founded.append((i, j + 1))
                matrix[i][j] = 0
                pygame.draw.rect(window, (255, 255, 255), (i * sq + 1, j * sq + 1, sq - 1, sq - 1))
    for i in founded:
        matrix[i] = 2
    time.sleep(0.1)
    founded = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                x, y = event.pos
                x = int(x / sq)
                y = int(y / sq)
                if x < w and y < h:
                    matrix[x][y] = 1
                    pygame.draw.rect(window, (0, 255, 0), (x * sq + 1, y * sq + 1, sq - 1, sq - 1))
                else:
                    response = requests.get("https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c0/Pudge_icon.png/revision/latest?cb=20160411211506")
                    img = pygame.image.load(io.BytesIO(response.content)).convert_alpha()
                    rect = img.get_rect(topleft=(200, 300))
                    window.fill((0, 0, 0))
                    text = font.render(f"pudge!!", True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    window.blit(img, rect)
                    pygame.display.flip()
                    time.sleep(0.5)
                    fill(255, 255, 255)
                    matrix = np.zeros((w, h))
            elif event.button == pygame.BUTTON_RIGHT:
                x, y = event.pos
                x = int(x / sq)
                y = int(y / sq)
                if x < w and y < h:
                    matrix[x][y] = 2
                    pygame.draw.rect(window, (255, 0, 0), (x * sq + 1, y * sq + 1, sq - 1, sq - 1))
                else:
                    response = requests.get("https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c0/Pudge_icon.png/revision/latest?cb=20160411211506")
                    img = pygame.image.load(io.BytesIO(response.content)).convert_alpha()
                    rect = img.get_rect(topleft=(200, 300))
                    window.fill((0, 0, 0))
                    text = font.render(f"pudge!!", True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    window.blit(img, rect)
                    pygame.display.flip()
                    time.sleep(0.5)
                    fill(255, 255, 255)
                    matrix = np.zeros((w, h))
            else:
                matrix = np.ones((w, h))
                fill(0, 255, 0)
    rx, ry = random.randint(0, w - 1), random.randint(0, h - 1)
    if matrix[rx][ry] == 0:
        matrix[rx][ry] = 1
    pygame.draw.rect(window, (0, 255, 0), (rx * sq + 1, ry * sq + 1, sq - 1, sq - 1))
    pygame.display.flip()