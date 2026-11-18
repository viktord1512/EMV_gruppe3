import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rumskib Simulation")

position = (400, 300)
box_size = (50, 50)
direction = (0, 0)
speed = 0.1

while True:
    screen.fill((255, 255, 255))
    rect = (position[0], position[1], box_size[0], box_size[1])
    pygame.draw.rect(screen, (0, 0, 0), rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = (-1, 0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = (1, 0)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                direction = (0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                direction = (0, 1)
                '''funktionen += 10 betyder at position flytter 10 pixels i den retning'''
        # print(f"Box position: {position}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        position = (position[0] + direction[0] * speed, position[1] + direction[1] * speed)

