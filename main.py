import pygame
import math
import numpy as np
from sys import exit

width = 800
height = 400
f_len = 700

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gradient Descend")
clock = pygame.time.Clock()

def TransposePoint(point: list[float]): 
    x, y = point
    return(x + width/2, y + height/2)

def ProjectPoint(point: list[float], f_len: float, theta: int):
    x, y, z = RotationTransformY(point, theta)
    offsety = 30

    projectionX = f_len*x / (z + f_len) + width/2
    projectionY = f_len*y / (z + f_len) + height/2 + offsety

    return (projectionX, projectionY)


def RotationTransformY(point: list[float], theta):
    theta = np.deg2rad(theta)
    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    rotated_point = R @ point
    return rotated_point


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
    points = ([a,a,perto],[a,b,perto],[b,a,perto],[b,b,perto],[a,a,longe],[a,b,longe],[b,a,longe],[b,b,longe],)
    points2 = ([a+105,a,perto],[a+105,b,perto],[b+105,a,perto],[b+105,b,perto],[a+105,a,longe],[a+105,b,longe],[b+105,a,longe],[b+105,b,longe],)
    # points = [RotationTransformY(point, angulo) for point in points]
    projections = [ProjectPoint(point, f_len, angulo) for point in points]
    projections2 = [ProjectPoint(point, f_len, angulo) for point in points2]
    
    # for point in points:
    #     pygame.draw.circle(screen, 'red', TransposePoint((point[0], point[1])), 5)



    for projection in projections:
        pygame.draw.circle(screen, 'blue', projection, 2, )
    for projection in projections2:
        pygame.draw.circle(screen, 'red', projection, 2)

    
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