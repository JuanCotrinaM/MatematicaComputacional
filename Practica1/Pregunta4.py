##Al presionar la tecla w el cubo va a rotar 30 grados con respecto a la recta 
##con direccion (1,1,1)
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0,0,1),(1,0,1),(1,0,0),(0,0,0),(0,1,1),(1,1,1),(1,1,0),(0,1,0)
    )

edges = (
    (0,1),(0,3),(0,4),(2,1),(2,6),(2,3),(5,4),(5,6),(5,1),(7,4),(7,6),(7,3)
    )
quads = (
	(0,1,2,3),(1,2,6,5),(2,6,7,3),(7,4,0,3),(0,1,5,4),(4,5,6,7)
	)
#define un cubo
def Cube():

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
#define un solido de cubo
def solidCube():

    glBegin(GL_QUADS)
    for quad in quads:
        for vertex in quad:
            glVertex3fv(vertices[vertex])
    glEnd()
#define las rectas cartesianas
def Recta():

	glBegin(GL_LINES)
	glVertex3fv((-5,0,0))
	glVertex3fv((2,0,0))
	glEnd()

	glBegin(GL_LINES)
	glVertex3fv((0,-3,0))
	glVertex3fv((0,3,0))
	glEnd()

	glBegin(GL_LINES)
	glVertex3fv((0,0,-3))
	glVertex3fv((0,0,3))
	glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]),0.1, 100.0)

    glTranslatef(-1,-0.5, -5)

    #angulo con el que se va a rotar el cubo
    angulo = 0;
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_w:
            		if angulo <360:
            			angulo +=30.0 
            			print(angulo)
            		else:
            			angulo = 0

#        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glColor(1,1,1,0)
        Recta()
        glColor(0,1,0,0)
        glPushMatrix()
        #el cubo se rota con angulo y con respecto a la recta (1,1,1) 
        glRotatef(angulo,1,1,1)
        #solidCube()
        Cube()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()