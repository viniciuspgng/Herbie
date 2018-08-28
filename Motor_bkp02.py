import RPi.GPIO as GPIO
import time
import pigpio

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

#Encoder de 20 faixas
EncoderDir = 19 #pino 35
EncoderEsq = 26 #pino 37

RotacaoDir = 0
RotacaoEsq = 0
TotalVolta = 20

#--------------------------------------------------------
# frente()
#--------------------------------------------------------
def frente( tempo =0.1):
    global RotacaoDir, RotacaoEsq
    Iniciando = True#(RotacaoEsq == 0 and RotacaoDir == 0)
    print("para Frente")

    if(Iniciando):
        GPIO.output(PinMotorDirA, GPIO.HIGH)
        GPIO.output(PinMotorDirB, GPIO.LOW)
        GPIO.output(PinMotorEsqA, GPIO.HIGH)
        GPIO.output(PinMotorEsqB, GPIO.LOW)
    else:
        if (RotacaoEsq <= RotacaoDir):
            GPIO.output(PinMotorDirA, GPIO.HIGH)
            GPIO.output(PinMotorDirB, GPIO.LOW)

        if (RotacaoDir <= RotacaoEsq):    
            GPIO.output(PinMotorEsqA, GPIO.HIGH)
            GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
# frenteEsq()
#--------------------------------------------------------
def frenteEsq( tempo =0.1 ):
    global RotacaoDir, RotacaoEsq
    
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
    global RotacaoDir, RotacaoEsq
    
    print("para direita")
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def reh(tempo=0.1):
    global RotacaoDir, RotacaoEsq
    
    print("para tras")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
        
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def rehDir(tempo =0.1):
    global RotacaoDir, RotacaoEsq
    
    print("para direita")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.LOW)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)
    time.sleep(tempo)
#--------------------------------------------------------
#--------------------------------------------------------
def rehEsq(tempo = 0.1):
    global RotacaoDir, RotacaoEsq
    
    print("para tras esquerda ")
    GPIO.output(PinMotorDirA, GPIO.LOW)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.LOW)
    GPIO.output(PinMotorEsqB, GPIO.LOW)
    time.sleep(tempo)

#--------------------------------------------------------
#--------------------------------------------------------
def stop():
    global RotacaoDir, RotacaoEsq
    
    print("Parado")
    GPIO.output(PinMotorDirA, GPIO.HIGH)
    GPIO.output(PinMotorDirB, GPIO.HIGH)
    GPIO.output(PinMotorEsqA, GPIO.HIGH)
    GPIO.output(PinMotorEsqB, GPIO.HIGH)

#--------------------------------------------------------
#--------------------------------------------------------
def start(nFrequencia = 2, nDutyCircle = 70):
    global RotacaoDir, RotacaoEsq
    PinsMotores = [PinMotorDirA, PinMotorDirB, PinMotorEsqA, PinMotorEsqB]
  
    ##GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    #Configura motor
    for A in PinsMotores:
        GPIO.setup(A, GPIO.OUT)
        GPIO.output(A, GPIO.LOW)
        if( A % 2 == 0):
            #Motor trabalha a 90RPM em 3V e 200RPM em 6V
            #90RPM = 1.5 Hz | 200RMP = 3.33Hz
            Aux = GPIO.PWM(PinMotorDirA, nFrequencia )#Frequencia
            Aux.start(nDutyCircle)#ChangeDutyCycle

    #Encoder
    GPIO.setup(EncoderDir,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(EncoderEsq,GPIO.IN,GPIO.PUD_UP)
        
    GPIO.add_event_detect( EncoderDir, GPIO.RISING, callback = CalculaVoltaRotaDireita )
    GPIO.add_event_detect( EncoderEsq, GPIO.RISING, callback = CalculaVoltaRotaEsquerda)

#--------------------------------------------------------
#--------------------------------------------------------
def restart(nFrequencia = 2, nDutyCircle = 70):
    global RotacaoDir, RotacaoEsq
    PinsMotores = [PinMotorDirA, PinMotorDirB, PinMotorEsqA, PinMotorEsqB]
  
    ##GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    #Configura motor
    for A in PinsMotores:
        #Motor trabalha a 90RPM em 3V e 200RPM em 6V
        #90RPM = 1.5 Hz | 200RMP = 3.33Hz
        Aux = GPIO.PWM(PinMotorDirA, nFrequencia )#Frequencia
        Aux.start(nDutyCircle)#ChangeDutyCycle

#--------------------------------------------------------
# clean()
#--------------------------------------------------------
def clean():
    
    # This command clears the configuration from the GPIO interface
    GPIO.cleanup()
#//    

#--------------------------------------------------------
# CalculaVolta()
#--------------------------------------------------------
def CalculaVoltaRotaDireita(porta):
    global RotacaoDir

    RotacaoDir += 1
    if( RotacaoDir > TotalVolta ):
        RotacaoDir = 0
        
def CalculaVoltaRotaEsquerda(porta):
    global RotacaoEsq

    RotacaoEsq += 1
    if( RotacaoEsq > TotalVolta ):
        RotacaoEsq = 0

start(30,100)

frente(3)
print("Esquerda ", str(RotacaoEsq), "\n")
print("Direita ", str(RotacaoDir), "\n")

print("Terminou")

# This command clears the configuration from the GPIO interface
clean()
#//
