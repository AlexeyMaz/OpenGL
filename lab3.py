import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw():
    glColor3f(0, 1, 0)
    glTranslatef(0, 0, -1)

    # "хвост"
    glutSolidSphere(0.08, 100, 100)
    glTranslatef(0, -0.09, 0.035)
    glutSolidSphere(0.12, 100, 100)
    glTranslatef(0, -0.12, 0.035)
    glutSolidSphere(0.17, 100, 100)
    glTranslatef(0, -0.14, 0.035)
    glutSolidSphere(0.2, 100, 100)

    # тело
    for i in range(10):
        glTranslatef(0, -0.14, 0)
        glutSolidSphere(0.2, 100, 100)

    # поднимающееся тело
    for i in range(4):
        glTranslatef(0, -0.12, 0.12)
        glutSolidSphere(0.2, 100, 100)

    # голова
    glTranslatef(0, -0.12, 0.12)
    glutSolidSphere(0.3, 100, 100)

    # глаза
    glPushMatrix()
    glColor3f(0, 0, 1)
    glTranslatef(-0.12, -0.22, 0.2)
    glRotatef(50, 1, 0, 0)
    glutSolidCylinder(0.1, 0.01, 100, 100)
    glTranslatef(0.25, 0, 0)
    glutSolidCylinder(0.1, 0.01, 100, 100)

    # зрачки
    glColor3f(0, 0, 0)
    glTranslatef(0, 0, 0.01)
    glutSolidCylinder(0.05, 0.01, 100, 100)
    glTranslatef(-0.25, 0, 0)
    glutSolidCylinder(0.05, 0.01, 100, 100)
    glPopMatrix()

    # рот
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(0, -0.31, -0.1)
    glRotatef(20, 1, 0, 0)
    glutSolidCylinder(0.2, 0.05, 100, 100)
    glPopMatrix()

    # рога
    glColor3f(0, 1, 0)
    glTranslatef(-0.1, 0.05, 0.25)
    glutSolidCylinder(0.01, 0.3, 100, 100)
    glTranslatef(0.2, 0, 0)
    glutSolidCylinder(0.01, 0.3, 100, 100)

    # glColor3f(1, 0.5, 0)
    glTranslatef(0, 0, 0.28)
    glutSolidSphere(0.03, 100, 100)
    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.03, 100, 100)


pygame.init()
display = (1200, 900)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glutInit(sys.argv)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

pygame.mouse.set_visible(False)
up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        ms = 0.06
        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, ms)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -ms)
        if keypress[pygame.K_d]:
            glTranslatef(-ms, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(ms, 0, 0)

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        draw()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
