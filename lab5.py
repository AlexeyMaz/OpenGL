from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global rot
global tran
global goingUp


class Material:
    def __init__(self, ar, ag, ab, dr, dg, db, sr, sg, sb, shn):
        self.ambient_r = ar
        self.ambient_g = ag
        self.ambient_b = ab
        self.diffuse_r = dr
        self.diffuse_g = dg
        self.diffuse_b = db
        self.specular_r = sr
        self.specular_g = sg
        self.specular_b = sb
        self.shine = shn

    def active(self):
        ambientt = [self.ambient_r, self.ambient_g, self.ambient_b, 1.0]
        glMaterialfv(GL_FRONT, GL_AMBIENT, ambientt)
        diffuse = [self.diffuse_r, self.diffuse_g, self.diffuse_b]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
        specular = [self.specular_r, self.specular_g, self.specular_b]
        glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
        glMaterialf(GL_FRONT, GL_SHININESS, self.shine * 128.0)


def drawBody():
    emerald = Material(0.0215, 0.1745, 0.0215, 0.07568, 0.61424, 0.07568, 0.633, 0.727811, 0.633, 0.6)
    silver = Material(0.19225, 0.19225, 0.19225, 0.50754, 0.50754, 0.50754, 0.508273, 0.508273, 0.508273, 0.4)
    chrome = Material(0.25, 0.25, 0.25, 0.4, 0.4, 0.4, 0.774597, 0.774597, 0.774597, 0.6)
    copper = Material(0.19125, 0.0735, 0.0225, 0.7038, 0.27048, 0.0828, 0.256777, 0.137622, 0.086014, 0.1)
    gold = Material(0.24725, 0.1995, 0.0745, 0.75164, 0.60648, 0.22648, 0.628281, 0.555802, 0.366065, 0.4)
    yrubber = Material(0.05, 0.05, 0, 0.05, 0.05, 0.4, 0.7, 0.7, 0.04, .078125)
    crubber = Material(0, 0.05, 0.05, 0.4, 0.5, 0.5, 0.04, 0.7, 0.7, .078125)
    chrome.active()

    glPushMatrix()

    glTranslatef(0, 0, tran / 100)
    glRotatef(rot, 0, 0, 1)
    glutSolidCube(0.9)

    glPopMatrix()


def init():
    global rot
    global tran
    global goingUp

    rot = 0
    tran = 0
    goingUp = True

    glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)

    light_diffuse = [0, 0, 1]
    light_pos = [0.0, 1.0, 0.0, 1.0]

    glEnable(GL_LIGHT2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT2, GL_POSITION, light_pos)
    glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
    glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
    glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.4)

    light_diffuse1 = [1, 0, 0]
    light_pos1 = [0.0, 0.0, 1.5, 1.0]

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos1)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.0)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.2)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.4)

    light_diffuse2 = [0, 1, 0]
    light_pos2 = [1.0, 0.0, 0.0, 1.0]

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse2)
    glLightfv(GL_LIGHT1, GL_POSITION, light_pos2)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.0)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.2)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.4)
    glEnable(GL_DEPTH_TEST)


def draw():
    global rot
    global tran
    global goingUp

    rot += 3
    if rot >= 630:
        rot = 0

    if tran >= 130:
        tran -= 3
        goingUp = False
    elif tran <= -130:
        tran += 3
        goingUp = True
    elif goingUp:
        tran += 3
    elif not goingUp:
        tran -= 3

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawBody()
    glutSwapBuffers()


def redraw():
    glutPostRedisplay()


def changeSize(w, h):
    if h == 0:
        h = 1
    ratio = 1.0 * w / h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)

    gluPerspective(45, ratio, 1, 1000)
    gluLookAt(3.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1200, 750)
glutInit(sys.argv)
glutCreateWindow('cube')
glutDisplayFunc(draw)
glutIdleFunc(redraw)
init()
glutReshapeFunc(changeSize)
glutMainLoop()
