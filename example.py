import pygame
import math
import numpy as np
from sys import exit

width = 800
height = 400
f_len = 160

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gradient Descend")
clock = pygame.time.Clock()

def TransposePoint(point: list[float]): 
    x, y = point
    return(x + width/2, y + height/2)

def ProjectPoint(point: list[float], f_len: float):
    x, y, z = point

    projectionX = f_len*x / (z + f_len)
    projectionY = f_len*y / (z + f_len)

    return (projectionX, projectionY)

def RotationTransform(point: list[float], angle):
    x, y, z = point
    x_rotated = x * math.cos(np.deg2rad( angle)) - z * math.sin(np.deg2rad(angle))
    z_rotated = x * math.sin(np.deg2rad(angle)) + z * math.cos(np.deg2rad(angle))
    print(angle)

    return (x_rotated, y, z_rotated)

a = -50
b = 50
perto = 50
longe = -50


angulo = 0
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    points = ([a , a, perto], [a,b,perto], [b,a,perto], [b,b,perto], [a, a, longe], [a,b,longe], [b,a,longe], [b,b,longe],)
    points = [RotationTransform(point, angulo) for point in points]
    projections = [ProjectPoint(point, f_len) for point in points]
    
    # for point in points:
    #     pygame.draw.circle(screen, 'red', TransposePoint((point[0], point[1])), 5)



    for projection in projections:
        pygame.draw.circle(screen, 'blue', TransposePoint(projection), 2)

    
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