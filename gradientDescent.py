import pygame
import math
import numpy as np
from sys import exit

import graphics

class GradientDescent:
    def __init__(self,pygame, screen,  screenDimentions: list[int], focalLength: float):
        self._screenDimentions = screenDimentions
        self._focalLength = focalLength
        self._pygame = pygame
        self._screen = screen

        self._XYZcolors = ['red', 'green', 'blue']

        # paralel = self.Parallelepiped((0, 0), 100, self._screenDimentions, self._focalLength)
        paralel = self.Parallelepiped((0, 0), 100, self._screenDimentions, self._focalLength)

        self._vertices = paralel.vertices
        self._edges = paralel.edges
        self._surfaces1 = paralel.surface1
        self._surfaces2 = paralel.surface2
        self._surfaces3 = paralel.surface3

    # def createParallelepipeds(self):




    class Parallelepiped:
        def __init__(self, pos: list[int], height: float, screenDimentions: list[int], focalLength: float):
            self._xpos, self._zpos = pos
            self._side = 100
            self._releaf = 5
            self._screenDimentions = screenDimentions
            self.focalLength = focalLength

            self.edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
            self.surfaces = [[1,2,6,5],[2,3,7,6],[4,5,6,7]]
            self.surface1 = [1,2,6,5]
            self.surface2 = [2,3,7,6]
            self.surface3 = [4,5,6,7]
            self.vertices = [ graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), 0, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self.focalLength), #|-
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, 0, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self.focalLength),#-|
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, 0, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self.focalLength),#_|
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), 0, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self.focalLength),#|_

                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), -height, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self.focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, -height, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self.focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, -height, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self.focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), -height, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self.focalLength),
            ]

            

        