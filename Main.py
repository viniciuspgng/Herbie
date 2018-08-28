import RPi.GPIO as GPIO
import time

DIREITA = 2
ESQUERDA = 1

# define which pins we are driving the L298N with

PinMotorDirA = 17 #pino 13
PinMotorDirB = 22 #pino 15
PinMotorEsqA = 24 #pino 16
PinMotorEsqB = 23 #pino 18

statusMotor = "Não foi realizado nenhuma operação"

def statusMotor():
    return print(statusMotor)
#--------------------------------------------------------
#--------------------------------------------------------
def motorFrente( tempo =0.1):
  
    statusMotor= "para Frente"
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
#--------------------------------------------------------
def motorFreteEsq( tempo =0.1 ):
    statusMotor= "para esquerda"
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def motorFreteDir( tempo =0.1):

    print("para direita")
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def motorRe(tempo=0.1):
    statusMotor= "para tras"
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
        
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def motorReDir(tempo =0.1):
    statusMotor= "para direita"
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def motorReEsq(tempo = 0.1):
    statusMotor= "para tras esquerda "
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
#--------------------------------------------------------
def stopMotors():
    statusMotor= "Parado"
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
    
# We're using the physical board pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(PinMotorDirA, GPIO.OUT)
GPIO.setup(PinMotorDirB, GPIO.OUT)
GPIO.setup(PinMotorEsqA, GPIO.OUT)
GPIO.setup(PinMotorEsqB, GPIO.OUT)

#Motor trabalha a 90RPM em 3V e 200RPM em 6V
#90RPM = 1.5 Hz | 200RMP = 3.33Hz
#PWMMotorDirA = GPIO.PWM(PinMotorDirA, 2 )#Frequencia
#PWMMotorDirB = GPIO.PWM(PinMotorDirB, 2 )#Frequencia
#PWMMotorEsqA = GPIO.PWM(PinMotorEsqA, 2 )#Frequencia
#PWMMotorEsqB = GPIO.PWM(PinMotorEsqB, 2 )#Frequencia

#PWMMotorDirA.start(70)#ChangeDutyCycle
#PWMMotorDirB.start(70)#ChangeDutyCycle
#PWMMotorEsqA.start(70)#ChangeDutyCycle
#PWMMotorEsqB.start(70)#ChangeDutyCycle

#print ("para tras")
#motorFrente(5)
#motorRe(5)

#esquerda
#motorVira(1,ESQUERDA)
#direita
#motorVira(1,DIREITA)

#motorFrente(3)

# This command clears the configuration from the GPIO interface
GPIO.cleanup()


