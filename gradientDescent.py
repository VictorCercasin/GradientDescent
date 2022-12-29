import math
import numpy as np
from numpy import random
from sys import exit

import graphics

class GradientDescent:
    def __init__(self,pygame, screen,  screenDimentions: list[int], focalLength: float):
        self._screenDimentions = screenDimentions
        self._focalLength = focalLength
        self._pygame = pygame
        self._screen = screen

        self.XYZcolors = ['red', 'green', 'blue'] #colors to display the axies

        self.vertices = []

        self.higher = -1000
        self.lower = 1000
        self.CreateGameArea()


    def CreateGameArea(self):
        createParallelsAt = ((0,0,200), (1,0,150), (0,1,150), (1,1,100))

        # for i, coords in enumerate(createParallelsAt):
        #     parallel = self.Parallelepiped((coords[0], coords[1]), coords[2], self._screenDimentions, self._focalLength)
        #     self.vertices.append(parallel.vertices)

        gradient = self.Gradient()
        for i in range(20):
            for j in range(20):
                parallel = self.Parallelepiped((i, j), gradient.get(i,j), self._screenDimentions, self._focalLength)
                self.vertices.append(parallel.vertices)
                if gradient.get(i,j) > self.higher:
                    self.higher = gradient.get(i,j)
                elif gradient.get(i,j) < self.lower:
                    self.lower = gradient.get(i,j)



    def RenderGameArea(self):
        rgb = (102, 0, 51)
        for i, parallel in enumerate(self.vertices):
            self._pygame.draw.polygon(self._screen, rgb, (parallel[self.Parallelepiped.surface1[0]].gamespaceCoordenates, parallel[self.Parallelepiped.surface1[1]].gamespaceCoordenates, parallel[self.Parallelepiped.surface1[2]].gamespaceCoordenates, parallel[self.Parallelepiped.surface1[3]].gamespaceCoordenates))
            self._pygame.draw.polygon(self._screen, [color*0.5 for color in rgb], (parallel[self.Parallelepiped.surface2[0]].gamespaceCoordenates, parallel[self.Parallelepiped.surface2[1]].gamespaceCoordenates, parallel[self.Parallelepiped.surface2[2]].gamespaceCoordenates, parallel[self.Parallelepiped.surface2[3]].gamespaceCoordenates))
            self._pygame.draw.polygon(self._screen, self.heatmap_color(-parallel[self.Parallelepiped.surface3[0]]._coordenates[1]), (parallel[self.Parallelepiped.surface3[0]].gamespaceCoordenates, parallel[self.Parallelepiped.surface3[1]].gamespaceCoordenates, parallel[self.Parallelepiped.surface3[2]].gamespaceCoordenates, parallel[self.Parallelepiped.surface3[3]].gamespaceCoordenates))

    def heatmap_color(self, value):

        if value < 0:
            value +=  abs( self.lower)
        value = value / self.higher

        hue = value * 240
        r, g, b = 0.0, 0.0, 0.0
        if hue < 60:
            r = 1.0
            g = hue / 60
        elif hue < 120:
            r = (120 - hue) / 60
            g = 1.0
        elif hue < 180:
            g = 1.0
            b = (hue - 120) / 60
        elif hue < 240:
            g = (240 - hue) / 60
            b = 1.0
        else:
            r = (hue - 240) / 60
            b = 1.0
        chroma = 1.0
        r = (r - 0.5) * chroma + 0.5
        g = (g - 0.5) * chroma + 0.5
        b = (b - 0.5) * chroma + 0.5
        return (r*255, g*255, b*255)


    class Parallelepiped:
        edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
        surfaces = [[1,2,6,5],[2,3,7,6],[4,5,6,7]]
        surface1 = [1,2,6,5]
        surface2 = [2,3,7,6]
        surface3 = [4,5,6,7]
        def __init__(self, pos: list[int], height: float, screenDimentions: list[int], focalLength: float):
            self._xpos, self._zpos = pos
            self._side = 10
            self._releaf = 3
            self._screenDimentions = screenDimentions
            self._focalLength = focalLength

            self.centerPos = [self._xpos * (self._side+self._releaf) + self._side/2, self._zpos * (self._side + self._releaf) + self._side/2]
            self.vertices = [ graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), 0, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self._focalLength), #|-
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, 0, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self._focalLength),#-|
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, 0, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self._focalLength),#_|
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), 0, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self._focalLength),#|_

                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), -height, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self._focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, -height, -self._zpos*(self._side+self._releaf)), self._screenDimentions, self._focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side, -height, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self._focalLength),
                              graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf), -height, -self._zpos*(self._side+self._releaf) - self._side), self._screenDimentions, self._focalLength),
            ]

    class Gradient:
        def __init__(self):
            self.get = self.generateFunction()
            self.modes = 100
            self.aRandomsX = [random.uniform(0,1) for n in range(self.modes)]
            self.bRandomsX = [random.uniform(0,1) for n in range(self.modes)]
            self.cRandomsX = [random.uniform(0, math.pi * 2) for n in range(self.modes)]

            self.aRandomsY = [random.uniform(0,1) for n in range(self.modes)]
            self.bRandomsY = [random.uniform(0,1) for n in range(self.modes)]
            self.cRandomsY = [random.uniform(0, math.pi * 2) for n in range(self.modes)]


        def generateFunction(self):

            def function(x, y):
                xComp = 0
                yComp = 0
                for i in range(self.modes):
                    xComp += self.aRandomsX[i] * (math.sin((x * self.bRandomsX[i]  + self.cRandomsX[i])) * 5)
                    yComp += self.aRandomsY[i] * (math.sin((y * self.bRandomsY[i] + self.cRandomsY[i])) * 5)
                return abs( xComp + yComp + 50)
            return function


        