import RPi.GPIO as GPIO
import time

DIREITA = 2
ESQUERDA = 1

# define which pins we are driving the L298N with

#PinMotorDirA = 17 #pino 11
#PinMotorDirB = 22 #pino 15
#PinMotorEsqA = 24 #pino 18
#PinMotorEsqB = 23 #pino 16

PinMotorDirA = 24 #pino 18
PinMotorDirB = 23 #pino 16
PinMotorEsqA = 17 #pino 11
PinMotorEsqB = 22 #pino 15

#--------------------------------------------------------
# frente()
#--------------------------------------------------------
def frente( tempo =0.1):
  
    print("para Frente")
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
# frenteEsq()
#--------------------------------------------------------
def frenteEsq( tempo =0.1 ):
    print("para esquerda")
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    
    time.sleep(tempo)
#--------------------------------------------------------
# frenteDir()
#--------------------------------------------------------
def frenteDir( tempo =0.1):

    print("para direita")
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def reh(tempo=0.1):
    print("para tras")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
        
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def rehDir(tempo =0.1):
    print("para direita")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def rehEsq(tempo = 0.1):
    print("para tras esquerda ")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
#--------------------------------------------------------
def stop():
    print("Parado")
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)

#--------------------------------------------------------
#--------------------------------------------------------
def start(nFrequencia = 2, nDutyCircle = 70):

    ##GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PinMotorDirA, GPIO.OUT)
    GPIO.setup(PinMotorDirB, GPIO.OUT)
    GPIO.setup(PinMotorEsqA, GPIO.OUT)
    GPIO.setup(PinMotorEsqB, GPIO.OUT)
    
    #Motor trabalha a 90RPM em 3V e 200RPM em 6V
    #90RPM = 1.5 Hz | 200RMP = 3.33Hz
    PWMMotorDirA = GPIO.PWM(PinMotorDirA, nFrequencia )#Frequencia
    PWMMotorDirB = GPIO.PWM(PinMotorDirB, nFrequencia )#Frequencia
    PWMMotorEsqA = GPIO.PWM(PinMotorEsqA, nFrequencia )#Frequencia
    PWMMotorEsqB = GPIO.PWM(PinMotorEsqB, nFrequencia )#Frequencia

    PWMMotorDirA.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorDirB.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorEsqA.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorEsqB.start(nDutyCircle)#ChangeDutyCycle

#--------------------------------------------------------
#--------------------------------------------------------
def restart(nFrequencia = 2, nDutyCircle = 70):

    PWMMotorDirA = GPIO.PWM(PinMotorDirA, nFrequencia )#Frequencia
    PWMMotorDirB = GPIO.PWM(PinMotorDirB, nFrequencia )#Frequencia
    PWMMotorEsqA = GPIO.PWM(PinMotorEsqA, nFrequencia )#Frequencia
    PWMMotorEsqB = GPIO.PWM(PinMotorEsqB, nFrequencia )#Frequencia

    PWMMotorDirA.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorDirB.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorEsqA.start(nDutyCircle)#ChangeDutyCycle
    PWMMotorEsqB.start(nDutyCircle)#ChangeDutyCycle

#--------------------------------------------------------
# clean()
#--------------------------------------------------------
def clean():
    # This command clears the configuration from the GPIO interface
    GPIO.cleanup()
#//    




#//frequencia(2)

#start()

#print ("para tras")
#freteEsq(5)
#freteDir(5)
#reh(1)


# This command clears the configuration from the GPIO interface
#clean()
#//
