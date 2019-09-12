from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

N1 = 100
N2 = 100
r1 = 2
ang2 = (2*math.pi)/N2 



def Pontos():
    getVertice = []
    getPontos = []
    
    for i in range(0,N1):
        ang =(i*math.pi/N1) - (math.pi/2) 
        lista1 = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        x = r1*math.cos(ang)
        y = r1*math.sin(ang)

        lista1.append(x) #popular a lista aux com x
        lista1.append(y) #popular a lista aux com y
        getVertice.append(lista1)
    
    for vertice in getVertice:
        r2 = vertice[0]

        for i in range(N2 + 1):
        
        

            x1 = r2 * math.cos(i* ang2)
            y1 = vertice[1]
            z1 = r2*math.sin(i*ang2)

            

            getPontos.append([x1,y1,z1])

    return getPontos



    



    



 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

getPontos = Pontos()
def Esfera():
    
    



    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    for Pontos in getPontos:
        glVertex3fv(Pontos)
       
    glEnd()
 
    
 

 

     
 
 
def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,2,3)
    Esfera()
    
    glutSwapBuffers()
   
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()