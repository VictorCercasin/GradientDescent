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
        self._parallelsPerSide = 20
        self._characterXYposition = {"x": random.randint(0,self._parallelsPerSide-1), "y": random.randint(0,self._parallelsPerSide-1)}

        self.XYZcolors = ['red', 'green', 'blue'] #colors to display the axies

        self.vertices = []
        self.parallels = [[0 for j in range(self._parallelsPerSide)] for i in range(self._parallelsPerSide)]

        self.higher = -1000
        self.lower = 1000
        self.CreateGameArea()


    def CreateGameArea(self):
        gradient = self.Gradient()
        for i in range(self._parallelsPerSide):
            for j in range(self._parallelsPerSide):
                parallel = self.Parallelepiped((i, j), gradient.get(i,j), self._screenDimentions, self._focalLength)
                if gradient.get(i,j) > self.higher:
                    self.higher = gradient.get(i,j)
                elif gradient.get(i,j) < self.lower:
                    self.lower = gradient.get(i,j)

        if(self.lower > 0):
            return
        newVertices = []
        newLower = 1000
        newHigher = -1000
        for i in range(self._parallelsPerSide):
            for j in range(self._parallelsPerSide):
                parallel = self.Parallelepiped((i, j), gradient.get(i,j) - self.lower, self._screenDimentions, self._focalLength)
                self.parallels[i][j] = parallel
                if gradient.get(i,j)   - self.lower > newHigher:
                    newHigher = gradient.get(i,j)  - self.lower
                elif gradient.get(i,j)   - self.lower < newLower:
                    newLower = gradient.get(i,j)  - self.lower
        self.lower = newLower
        self.higher = newHigher




    def RenderGameArea(self):
        rgb = (20, 20, 20)
        centerPoint = self.parallels[self._characterXYposition["x"]][self._characterXYposition["y"]].centerPoint

        self.sortRenderingOrder(self.parallels, centerPoint)


        for i in range(self._parallelsPerSide):
            for j in range(self._parallelsPerSide):
                self._pygame.draw.polygon(self._screen, rgb, (self.parallels[i][j].vertices[self.Parallelepiped.surface1[0]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface1[1]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface1[2]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface1[3]].gamespaceCoordenates))
                self._pygame.draw.polygon(self._screen, [color*0.5 for color in rgb], (self.parallels[i][j].vertices[self.Parallelepiped.surface2[0]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface2[1]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface2[2]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface2[3]].gamespaceCoordenates))
                self._pygame.draw.polygon(self._screen, self.heatmap_color(-self.parallels[i][j].vertices[self.Parallelepiped.surface3[0]]._coordenates[1]), (self.parallels[i][j].vertices[self.Parallelepiped.surface3[0]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface3[1]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface3[2]].gamespaceCoordenates, self.parallels[i][j].vertices[self.Parallelepiped.surface3[3]].gamespaceCoordenates))
        
        self._pygame.draw.circle(self._screen, 'red', centerPoint.gamespaceCoordenates, 1)
        


    def heatmap_color(self, value):
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
        if r > 1:
            r = 1
        g = (g - 0.5) * chroma + 0.5
        if g > 1:
            g = 1
        b = (b - 0.5) * chroma + 0.5
        if b > 1:
            b = 1
        if r < 0:
            r = 0
        g = (g - 0.5) * chroma + 0.5
        if g < 0:
            g = 0
        b = (b - 0.5) * chroma + 0.5
        if b < 0:
            b = 0

        return (r*255, g*255, b*255)

    def sortRenderingOrder(self, parallels, centerPint):
        print(parallels[0][0].vertices[self.Parallelepiped.surface1[0]]._rotatedCoordenates)


    class Parallelepiped:
        edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
        surfaces = [[1,2,6,5],[2,3,7,6],[4,5,6,7]]
        surface1 = [1,2,6,5]
        surface2 = [2,3,7,6]
        surface3 = [4,5,6,7]

        surface4 = [0,4,7,3]
        surface5 = [0,4,5,1]

        def __init__(self, pos: list[int], height: float, screenDimentions: list[int], focalLength: float):
            self._xpos, self._zpos = pos
            self._height = height
            self._side = 10
            self._releaf = 3
            self._screenDimentions = screenDimentions
            self._focalLength = focalLength

            self.centerPos = [self._xpos * (self._side+self._releaf) + self._side/2, self._zpos * (self._side + self._releaf) + self._side/2]
            self.centerPoint = graphics.PointInGameSpace ((self._xpos*(self._side+self._releaf) + self._side/2, -height, -self._zpos*(self._side+self._releaf) - self._side/2), self._screenDimentions, self._focalLength)


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
            #number of wave modes
            self.modes = 30
            #gradient amplitude multiplier
            self.multiplier = 5

            #Changes amplitude of the mode
            self.modeMultiplier = [random.uniform(1,1) for n in range(self.modes)]
            #xMultiplier and yMultiplier shift the wave angle in relation the the X and Y axies
            self.xMultiplier = [random.uniform(-1,1) for n in range(self.modes)]
            self.yMultiplier = [random.uniform(-1,1) for n in range(self.modes)]
            #determines the possible frequency space. the higher the top range, higher the frequency
            self.frequencySpace = [random.uniform(0,0.7) for n in range(self.modes)]
            self.phaseShifter = [random.uniform(0, math.pi * 2) for n in range(self.modes)]



        def generateFunction(self):

            def function(x, y):
                xComp = 0
                yComp = 0
                xyComp = 0
                for i in range(self.modes):
                    xyComp += self.modeMultiplier[i] * (math.sin(((self.xMultiplier[i]*x +self.yMultiplier[i]*y) * self.frequencySpace[i] + self.phaseShifter[i])) * self.multiplier)
                return  xComp + yComp + xyComp
            return function


        