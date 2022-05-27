#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:04:25 2022

@author: szabi
"""
import numpy as np
import matplotlib.pyplot as plt
class PolygonDrawer(object):
    def __init__(self,ax,startx=100,starty=100):
        self.polygon = []
        self.x=startx
        self.y=starty
        self.ax=ax
    def draw_line(self):
        self.polygon.append((self.x,self.y))
        xy = plt.ginput(1)

        x = xy[0][0]
        y = xy[0][1]
        self.ax.plot((self.x,x),(self.y,y))
        self.ax.figure.canvas.draw()
        self.x=x
        self.y=y


maxx=5
maxy=5
fig = plt.figure()
ax = plt.axes(xticks=np.linspace(-maxx,maxx,11),yticks=np.linspace(-maxy,maxy,11))
ax.set_autoscale_on(False)
pd = PolygonDrawer(ax,startx=-maxx, starty=-maxy)
for i in range(0,10):
    pd.draw_line() # here you click on the plot
    print(i)

height=5
waypoints=[[p[0],p[1],height] for p in pd.polygon]
