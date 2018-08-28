import RPi.GPIO as GPIO
import time

DIREITA = 2
ESQUERDA = 1

# define which pins we are driving the L298N with

PinMotorDirA = 17 #pino 13
MotorAPinTwo = 22 #pino 15
MotorBPinOne = 24 #pino 16
MotorBPinTwo = 23 #pino 18

###
def motorFrente( tempo,direcao=3 ):

  
    if (direcao == ESQUERDA):#ESQUERDA
        print("para esquerda")
        GPIO.output(MotorBPinOne, GPIO.HIGH)
        GPIO.output(MotorBPinTwo, GPIO.LOW)
        GPIO.output(PinMotorDirA, GPIO.LOW)
        GPIO.output(MotorAPinTwo, GPIO.LOW)
        
    elif (direcao == DIREITA):
        print("para direita")
        GPIO.output(MotorBPinOne, GPIO.LOW)
        GPIO.output(MotorBPinTwo, GPIO.LOW)
        GPIO.output(PinMotorDirA, GPIO.HIGH)
        GPIO.output(MotorAPinTwo, GPIO.LOW)
    else:
        print("para Frente")
        GPIO.output(PinMotorDirA, GPIO.HIGH)
        GPIO.output(MotorAPinTwo, GPIO.LOW)
        GPIO.output(MotorBPinOne, GPIO.HIGH)
        GPIO.output(MotorBPinTwo, GPIO.LOW)
    time.sleep(3)
###
def motorRe(tempo,direcao=3):
    if (direcao == DIREITA):
        print("para direita")
        GPIO.output(PinMotorDirA, GPIO.LOW)
        GPIO.output(MotorAPinTwo, GPIO.LOW)
        GPIO.output(MotorBPinOne, GPIO.LOW)
        GPIO.output(MotorBPinTwo, GPIO.HIGH)
    elif (direcao == ESQUERDA):
        print("para tras esquerda ")
        GPIO.output(PinMotorDirA, GPIO.LOW)
        GPIO.output(MotorAPinTwo, GPIO.HIGH)
        GPIO.output(MotorBPinOne, GPIO.LOW)
        GPIO.output(MotorBPinTwo, GPIO.LOW)
    else:
        print("para tras")
        GPIO.output(PinMotorDirA, GPIO.LOW)
        GPIO.output(MotorAPinTwo, GPIO.HIGH)
        GPIO.output(MotorBPinOne, GPIO.LOW)
        GPIO.output(MotorBPinTwo, GPIO.HIGH)
        
    time.sleep(2)
  
###
def stopMotors():
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(MotorAPinTwo, GPIO.HIGH)
    GPIO.output(MotorBPinOne, GPIO.HIGH)
    GPIO.output(MotorBPinTwo, GPIO.HIGH)
    

