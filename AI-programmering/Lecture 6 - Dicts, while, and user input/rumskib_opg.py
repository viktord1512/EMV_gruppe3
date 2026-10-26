import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rumskib Simulation")

box_position = [400, 300]
box_size = [50, 50]

box_speed = 5

while True:
    screen.fill((255, 255, 255))
    rect = box_position + box_size
    pygame.draw.rect(screen, (0, 0, 0), rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_position[0] -= 10
            if event.key == pygame.K_RIGHT:
                box_position[0] += 10
            if event.key == pygame.K_UP:
                box_position[1] -= 10
            if event.key == pygame.K_DOWN:
                box_position[1] += 10
                '''funktionen += 10 betyder at box_position flytter 10 pixels i den retning'''
        print(f"Box position: {box_position}")
