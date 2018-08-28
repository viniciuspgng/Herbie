import numpy as np
import cv2
import time
#?import Motor as mv

from RemoteDebugFeature import RemoteDebug

FATOR_MOTOR = 40
minLineLength = 50
maxLineGap = 30

lower_red = np.array([0,70,50])#np.array([30,150,50])
upper_red = np.array([10,255,255])#np.array([255,255,180])

r = 0
h = 240
c = 80
w = 140

def deploy():
    cam.release()
    cv2.destroyAllWindows()
    #?motor.clean()
    #?del motor

#
#
#
#
def AnalisaImagemRMA(frame):
    Executa = True
    Tentativa = 0
    left = 0
    right = 0
    
    
    #Corta a imagem capiturada
    #roi = frame[r:r+h, c:c+w]
    #Da imagem trasforma as configurações de cores de RGB para HSV
    hsv = cv2.GaussianBlur(hsv, (21, 21), 0)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    #Cria uma mascara para colher imagem no intervalo de HSV conforme os dois array
    image_mask=cv2.inRange(hsv,lower_red,upper_red)

    frameBin = cv2.threshold(image_mask, LimiarBinarizacao,255, cv2.THRESH_BINARY)[1]
    frameBin = cv2.dilate(frameBin, None, iterations=2)
    frameBin = cv2.bitwise_not(frameBin)
    #output=cv2.bitwise_and(frame,frame,mask=image_mask)

    #Realiaza verificação de linhas
    edges = cv2.Canny(output,50,150,apertureSize=3)
     
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
            #Esquerda y2    #Direita y1
            print(y1, y2)
            left = y2
            right= y1

            #Esquerda y2    #Direita y1
            print("ESQUERDA: " + str(left), "DIREITA: " + str(right))

            if( ((right - left) >= 0) and (FATOR_MOTOR >= (right - left) and (right - left) <= FATOR_MOTOR)):
                print("Motor frente 1")
                #?motor.frente(0.3)
                #motor.frente(10)

            elif( ((left - right) >= 0) and (FATOR_MOTOR >= (left - right) and (left - right) <= FATOR_MOTOR)):
                print("Motor frente 2")
                #?motor.frente(0.3)
                #motor.frente(10)
            elif(right < left):
                print("Motor frente esquerda")
                #?motor.frenteEsq(0.3)
            elif(right > left):
                print("Motor frente direita")
                #?motor.frenteDir(0.3)
            elif( right <= 0  or left <= 0 ):
                print("Parar Motor 1")
                
    #motor.stop()
    #cv2.imshow('Original',frame)
    #cv2.imshow('Canny',edges)

    #cv2.imshow('filter', roi)
        
    #cv2.imshow('Output',output)
    #motor.clean()
     
    return left, right

###----------------------------------------
###   MAIN
###----------------------------------------
if (__name__ == "__main__"):
    ##### REMOTE DEBUG CALL #####
 
    remote_debug = True
    if remote_debug == True:
            RemoteDebug()   
 
    ###############################
    #Defica cam como objeto da camera
    cam = cv2.VideoCapture(0)
    #resolução da camera em 320x240
    cam.set(3,320)
    cam.set(4,240)
    
    #instancia classe motores
    #?motor = mv.motores(24,23,17,22,26,19,6,13)
    #?motor.start(180,60,180,55)
    
    #faz algumas leituras de frames antes de consierar a analise
    #motivo: algumas camera podem demorar mais para se "acosumar a luminosidade" quando ligam, capturando frames consecutivos com muita variacao de luminosidade. Para nao levar este efeito ao processamento de imagem, capturas sucessivas sao feitas fora do processamento da imagem, dando tempo para a camera "se acostumar" a luminosidade do ambiente
    for i in range(0,20):
        #Captura imagem da camera
        ret, frame = cam.read()
    
    while ( True ):
    
        try:
            #Captura imagem da camera
            ret, frame = cam.read()
            
            if (ret):
                left, right = AnalisaImagemRMA()
    
                
        except Exception as e:
            print("Houve um problema inesperado, operação reexecutará em 10 segundos, segue detalhe do erro:")
            print (str(e))
            time.sleep(10)
        
        if cv2.waitKey(1) == 27:
           break
    
    deploy()
