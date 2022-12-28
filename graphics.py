import pygame
import math
import numpy as np
from sys import exit

def ProjectPoint(point: list[float], f_len: float, screenDimentions: int, theta: int):
    x, y, z =point
    width, height = screenDimentions

    x, y, z = RotationTransformY(point, 45)
    x, y, z = RotationTransformX((x, y, z), 30)
    # x, y, z = RotationTransformZ((x, y, z), 10)

    offsety = 30

    projectionX = f_len*x / (z + f_len) + width/2
    projectionY = f_len*y / (z + f_len) + height/2 + offsety

    return (projectionX, projectionY)


def RotationTransformX(point: list[float], theta):
    theta = np.deg2rad(theta)
    R = np.array([[1, 0, 0],
                  [0, math.cos(theta), math.sin(-theta)],
                  [0, math.sin(theta), math.cos(theta)]])
    rotated_point = R @ point
    return rotated_point

def RotationTransformY(point: list[float], theta):
    theta = np.deg2rad(theta)
    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    rotated_point = R @ point
    return rotated_point

def RotationTransformZ(point: list[float], theta):
    theta = np.deg2rad(theta)
    R = np.array([[math.cos(theta), math.sin(-theta), 0],
                  [np.sin(theta), math.cos(theta), 0],
                  [0, 0, 1]])
    rotated_point = R @ point
    return rotated_point


class PointInGameSpace:
    def __init__(self, coordenates: list[float], screenDimentions: list[int], focalLength: float):
        self._coordenates = coordenates
        self._screenDimentions = screenDimentions
        self._focalLength = focalLength

        self._gamespaceCoordenates = self.ProjectPointInGameSpace(self._coordenates, self._screenDimentions, self._focalLength)


    def ProjectPointInGameSpace(self, coordenates: list[float],screenDimentions: list[int],focalLength: int):
        width, height = screenDimentions

        x, y, z = RotationTransformY(coordenates, 45)
        x, y, z = RotationTransformX((x, y, z), 30)
        # x, y, z = coordenates

        offsety = 30

        projectionX = focalLength*x / (z + focalLength) + width/2
        projectionY = focalLength*y / (z + focalLength) + height/2 + offsety

        return (projectionX, projectionY)
    
    def get2DCoordenates(self):
        return self._gamespaceCoordenates