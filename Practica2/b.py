
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

pto_control = np.array([[-3.0,0.0],[-1.0,4.0],[2.0,3.0],[4.0,1.0]])
n,m = pto_control.shape

##algoritmo de De Bezier
def PtoBezier(vertices, t, n):

    pto_aux = np.copy(vertices)
   
    for k in range (1,n-1):
        for i in range(n-k):
            pto_aux[i][0] = (1 - t)*pto_aux[i][0] + t*pto_aux[i+1][0]
            pto_aux[i][1] = (1 - t)*pto_aux[i][1] + t*pto_aux[i+1][1]

    return pto_aux[0]
 
def drawOriginalCurve():

    incr = 0.001
    glColor(1.0,0.0,0.0)

    glBegin(GL_LINE_STRIP)

    t = 0.0
    while t < 1.0 :
        p = PtoBezier(pto_control,t,n)
        glVertex2f(p[0], p[1])
        t += incr
    glVertex2f(pto_control[n-1][0],pto_control[n-1][1])
    
    glEnd()
    glFlush()

   
def drawPtoControl():

    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5.0)

    glBegin(GL_POINTS)

    for i in range(n):
        glVertex2f(pto_control[i][0],pto_control[i][1])

    glEnd()

#Muestra los puntos de control y la curva de bezier
def drawBezier():
    
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT)

    drawPtoControl()
    drawOriginalCurve()

    glFlush()

#define las rectas cartesianas
def Recta():

    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex3fv((-5,0,0))
    glVertex3fv((5,0,0))
    glEnd()

    glBegin(GL_LINES)
    glVertex3fv((0,-5,0))
    glVertex3fv((0,5,0))
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    ###Creacion de puntos de control
    global pto_control
    global n

    gluPerspective(30, (display[0]/display[1]),0.1, 30.0)

    glTranslatef(-1,-0.5, -30)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        drawBezier()
        Recta()

        pygame.display.flip()
        pygame.time.wait(10)

main()
