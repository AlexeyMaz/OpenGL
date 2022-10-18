import pygame as pg
import pygame.key
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

    scale = 1.0 / 16.0
    while True:
        keys = pygame.key.get_pressed()
        glTranslatef(scale * 2.5, scale * 2.5, 0)
        if keys[K_LEFT]:
            glRotate(-0.2, 0, 0, 1)
        if keys[K_RIGHT]:
            glRotate(0.2, 0, 0, 1)
        if keys[K_UP]:
            glRotate(-0.2, 1, 0, 0)
        if keys[K_DOWN]:
            glRotate(0.2, 1, 0, 1)
        glTranslatef(scale * -2.5, scale * -2.5, 0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rect()
        triangles()
        pg.display.flip()


main()
# легковая машина
