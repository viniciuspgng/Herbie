import numpy as np
import cv2
import time
import Motor
import sys

NAO_ENCONTROU = 1
FINALIZOU = 2
FATOR_MOTOR = 80

lower_red1 = np.array([0,100,80])#np.array([30,150,50])
upper_red1 = np.array([10,256,256])#np.array([255,255,180])
lower_red2 = np.array([170,100,80])#np.array([30,150,50])
upper_red2 = np.array([180,256,256])#np.array([255,255,180])

#Defica cam como objeto da camera
cam = cv2.VideoCapture(0)
##cam = cv2.VideoCapture('/home/pi/Projeto RAMLC/RMA Oficial/V_20170812_101753.mp4')
#resolução da camera em 320x240
heigth=320
width=240

cam.set(3,heigth)
cam.set(4,width)

#motor = Motor.motores(24,23,17,22,26,19)

#corte da visao da camera
r = 0
h = 240
c = 80
w = 200

def deploy():
    cam.release()
    cv2.destroyAllWindows()
    
    #motor.clean()
    #del motor

def varrerAteFaixa():
    Executa = True
    Tentativa = 0
    left = 0
    right = 0

    ret, frame = cam.read()
    #Corta a imagem capiturada
    roi = frame[r:r+h, c:c+w]
    
    #Da imagem trasforma as configurações de cores de RGB para HSV
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    #Efeito de blur para retirar imperfeição
    #blur = cv2.blur(hsv,(5,5))
    #blur = cv2.GaussianBlur(hsv,(3,3), 0)
        
    #Cria uma mascara para colher imagem no intervalo de HSV conforme os dois array
    image_mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    image_mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    image_mask = image_mask1 + image_mask2
    output=cv2.bitwise_and(roi,roi,mask=image_mask)

    #Efeito de blur para retirar imperfeição
    smoothed = cv2.blur(output,(1,1))
    #Realiaza verificação de linhas
    edges = cv2.Canny(smoothed,50,150,apertureSize=3)
     
    lines = cv2.HoughLines(edges,1,np.pi/180,80)
    if lines is not None:
        Tentativa = 0
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))#direita
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))#Equerda
            y2 = int(y0 - 1000*(a))
            cv2.line(edges,(x1,y1),(x2,y2),(0,0,255),2)

            left = y2
            right= y1
            #if(y2<=0):
            #    left = y2*-1
            #if(y1<= 0):
            #    right= y1*-1
                
    #cv2.imshow('Original',frame)
    #cv2.imshow('Canny',edges)

    #cv2.imshow('filter', roi)
        
    #cv2.imshow('Output',edges)
     
    return right, left

#########################
#         MAIN          #
#########################



#motor.start(100,255)

#faz algumas leituras de frames antes de consierar a analise
#motivo: algumas camera podem demorar mais para se "acosumar a luminosidade" quando ligam, capturando frames consecutivos com muita variacao de luminosidade. Para nao levar este efeito ao processamento de imagem, capturas sucessivas sao feitas fora do processamento da imagem, dando tempo para a camera "se acostumar" a luminosidade do ambiente
#for i in range(0,20):
#    ret, Frame = cam.read()

while ( True ):
    try:
        right, left = varrerAteFaixa()
        if(True):
            #Esquerda y2    #Direita y1
            print("ESQUERDA: " + str(left), "DIREITA: " + str(right))

            if( ((right - left) >= 0) and (FATOR_MOTOR >= (right - left) and (right - left) <= FATOR_MOTOR)):
                print("Motor frente 1")
                      
                #motor.frente(0.2)
                #motor.frente(10)

            elif( ((left - right) >= 0) and (FATOR_MOTOR >= (left - right) and (left - right) <= FATOR_MOTOR)):
                print("Motor frente 2")
               
                #motor.frente(0.2)
                #motor.frente(10)
            elif(right < left):
                print("Motor frente esquerda")
                #motor.frenteEsq(0.2)

            elif(right > left):
                print("Motor frente direita")
                #motor.frenteDir(0.2)
            elif( right <= 0  or left <= 0 ):
                print("Parar Motor 1")
                #motor.stop()
                
            ##elif( y1 < 0 or y2 < 0 ):
             ##   print("Localizado ponto vertical")
            
            #if(status == NAO_ENCONTROU)
            print("EXECUTANDO NOVO CICLO")
            if cv2.waitKey(33) == 27:
               break

    except Exception as e:
        print("Houve um problema inesperado, operação reexecutará em 10 segundos, segue detalhe do erro:")
        print (str(e))
        time.sleep(10)
        sys.exc_info()
        pass
    finally:
        deploy()
        exit(1)
