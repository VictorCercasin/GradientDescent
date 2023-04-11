import pygame
import math
import numpy as np
from sys import exit

import graphics
import gradientDescent

width = 1000
height = 500
screenDimentions = [width, height]
focalLength = 700

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gradient Descend")
clock = pygame.time.Clock()



angulo = 0

gradiente = gradientDescent.GradientDescent(pygame, screen, screenDimentions, focalLength)


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit

    gradiente.RenderGameArea()
  
    if(angulo < 360):
        angulo += 1
    else:
        angulo = 0

    pygame.display.update()
    clock.tick(60)