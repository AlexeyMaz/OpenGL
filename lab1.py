import pygame as pg
from pygame.locals import *
from OpenGL.GL import *


def rect():
    glBegin(GL_QUADS)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)
    glVertex2f(-0.6, 1)
    glVertex2f(-0.6, -1)
    glEnd()


def triangles():
    glBegin(GL_TRIANGLES)
    x12, x3, y1, y2, y3 = -0.6, -0.3, 1, 0.6, 0.8
    for i in range(5):
        glVertex2f(x12, y1)
        glVertex2f(x12, y2)
        glVertex2f(x3, y3)
        y1 = y2
        y2 -= 0.4
        y3 -= 0.4
    glEnd()


def main():
    pg.init()
    display = (1280, 720)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 0.0, 0.0, 0.0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rect()
        triangles()
        pg.display.flip()


main()
