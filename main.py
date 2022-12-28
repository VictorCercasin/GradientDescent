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





a = -50
b = 50
perto = 50
longe = -50


angulo = 0

teste = gradientDescent.GradientDescent(pygame, screen, screenDimentions, focalLength)


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    # for i, surface in enumerate(teste._surfaces):
    #     print(teste._vertices[surface[0]].get2DCoordenates())
    #     pygame.draw.polygon(screen, 'green', (teste._vertices[surface[0]].get2DCoordenates(),teste._vertices[surface[1]].get2DCoordenates(),teste._vertices[surface[2]].get2DCoordenates(),teste._vertices[surface[3]].get2DCoordenates()))

    for i, edge in enumerate(teste._edges):
        pygame.draw.line(screen, 'white', teste._vertices[edge[0]].get2DCoordenates(), teste._vertices[edge[1]].get2DCoordenates(), 10)

    pygame.draw.polygon(screen, 'green', (teste._vertices[teste._surfaces1[0]].get2DCoordenates(), teste._vertices[teste._surfaces1[1]].get2DCoordenates(), teste._vertices[teste._surfaces1[2]].get2DCoordenates(), teste._vertices[teste._surfaces1[3]].get2DCoordenates()))
    pygame.draw.polygon(screen, 'blue', (teste._vertices[teste._surfaces2[0]].get2DCoordenates(), teste._vertices[teste._surfaces2[1]].get2DCoordenates(), teste._vertices[teste._surfaces2[2]].get2DCoordenates(), teste._vertices[teste._surfaces2[3]].get2DCoordenates()))
    pygame.draw.polygon(screen, 'red', (teste._vertices[teste._surfaces3[0]].get2DCoordenates(), teste._vertices[teste._surfaces3[1]].get2DCoordenates(), teste._vertices[teste._surfaces3[2]].get2DCoordenates(), teste._vertices[teste._surfaces3[3]].get2DCoordenates()))





    # points = ([a,a,perto],[b,a,perto],[b,b,perto],[a,b,perto],[a,a,longe],[b,a,longe],[b,b,longe],[a,b,longe],)
    # points2 = ([a+105,a,perto],[b+105,a,perto],[b+105,b,perto],[a+105,b,perto],[a+105,a,longe],[b+105,a,longe],[b+105,b,longe],[a+105,b,longe],)
    # points3 = ([a,a,perto-105],[b,a,perto-105],[b,b,perto-105],[a,b,perto-105],[a,a,longe-105],[b,a,longe-105],[b,b,longe-105],[a,b,longe-105],)
    # edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[5,1],[6,2],[7,3]]
    # surfaces = [[4,5,6,7]]
    # # points = [RotationTransformY(point, angulo) for point in points]
    # projections = [graphics.PointInGameSpace(point, screenDimentions, focalLength).get2DCoordenates() for point in points]
    # projections2 = [graphics.PointInGameSpace(point, screenDimentions, focalLength).get2DCoordenates() for point in points2]
    # projections3 = [graphics.PointInGameSpace(point, screenDimentions, focalLength).get2DCoordenates() for point in points3]

    colors=['blue', 'blue', 'blue', 'blue', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green',]



            
    # for i, edge in enumerate(edges):
    #     pygame.draw.line(screen, colors[i % len(colors)], projections[edges[i][0]], projections[edges[i][1]])
    # for i, edge in enumerate(edges):
    #     pygame.draw.line(screen, colors[i % len(colors)], projections2[edges[i][0]], projections2[edges[i][1]])
    # for i, edge in enumerate(edges):
    #     pygame.draw.line(screen, colors[i % len(colors)], projections3[edges[i][0]], projections3[edges[i][1]])



    
    if(angulo < 360):
        angulo += 1
    else:
        angulo = 0

    # if(f_len < 1000 and cresce):
    #     f_len += 10
    # else:
    #     cresce = False
    # if(f_len > 100 and not cresce):
    #     f_len -= 10
    # else:
    #     cresce = True


    pygame.display.update()
    clock.tick(60)