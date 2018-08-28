import time
import pigpio

LOW = 0
HIGH = 1

class motores:

    motorAIn = 24 #pino 18
    motorAOut = 23 #pino 16
    motorBIn = 17 #pino 11
    motorBOut = 22 #pino 15
    
    #Encoder de 20 faixas
    encoderA = 26 #pino 37
    encoderB = 19 #pino 35

    callbackEsq = None
    callbackDir = None
    RotacaoDir = 0
    RotacaoEsq = 0
    TotalVolta = 20
    pos = 0
    pi = None#pigpio.pi()

      
    # define which pins we are driving the L298N with

    #motorAOut = 17 #pino 11
    #motorAIn = 22 #pino 15
    #motorBIn = 24 #pino 18
    #motorBOut = 23 #pino 16
    def __init__(self, pmotorAIn=None, pmotorAOut=None, pmotorBIn=None, pmotorBOut=None, pencoderA=None, pencoderB=None ):

        self.motorAIn  = (self.motorAIn  if (pmotorAIn == None)  else pmotorAIn)
        self.motorAOut = (self.motorAIn  if (pmotorAOut == None) else pmotorAOut)
        self.motorBIn  = (self.motorBIn  if (pmotorBIn == None)  else pmotorBIn)
        self.motorBOut = (self.motorBOut if (pmotorBOut == None) else pmotorBOut)
        self.encoderA  = (self.encoderA  if (pencoderA == None)  else pencoderA)
        self.encoderB  = (self.encoderB  if (pencoderB == None)  else pencoderB)

    #--------------------------------------------------------
    # frente()
    #--------------------------------------------------------
    def frente(self, tempo =0.1):

        print("para Frente")

        if (self.RotacaoEsq < self.RotacaoDir):
            self.pi.write(self.motorBIn, HIGH)
            self.pi.write(self.motorBOut, LOW)

        elif (self.RotacaoEsq > self.RotacaoDir):    
            self.pi.write(self.motorAIn, HIGH)
            self.pi.write(self.motorAOut, LOW)
            
        else:
            self.pi.write(self.motorAIn, HIGH)
            self.pi.write(self.motorAOut, LOW)
            self.pi.write(self.motorBIn, HIGH)
            self.pi.write(self.motorBOut, LOW)

        time.sleep(tempo)
        self.stop()

    #--------------------------------------------------------
    # frenteEsq()
    #--------------------------------------------------------
    def frenteEsq( self,tempo =0.1 ):
        
        print("para esquerda")
            
        self.pi.write(self.motorBIn, HIGH)
        self.pi.write(self.motorBOut, LOW)

        time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    # frenteDir()
    #--------------------------------------------------------
    def frenteDir( self,tempo =0.1):
        
        print("para direita")
        self.pi.write(self.motorAIn, HIGH)
        self.pi.write(self.motorAOut, LOW)

        time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def reh(self, tempo=0.1):
        
        print("para tras")
        if (self.RotacaoEsq < self.RotacaoDir):
            self.pi.write(self.motorBIn, LOW)
            self.pi.write(self.motorBOut, HIGH)

        elif (self.RotacaoEsq > self.RotacaoDir):    
            self.pi.write(self.motorAIn, LOW)
            self.pi.write(self.motorAOut, HIGH)
            
        else:
            self.pi.write(self.motorAIn, LOW)
            self.pi.write(self.motorAOut, HIGH)
            self.pi.write(self.motorBIn, LOW)
            self.pi.write(self.motorBOut, HIGH)

        time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def rehDir(self,tempo =0.1):
        
        print("re para direita")
        self.pi.write(self.motorBIn, LOW)
        self.pi.write(self.motorBOut, HIGH)

        time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def rehEsq(tempo = 0.1):
        
        print("re para tras esquerda ")
        self.pi.write(self.motorAOut, LOW)
        self.pi.write(self.motorAIn, HIGH)

        time.sleep(tempo)
        self.stop()

    #--------------------------------------------------------
    #--------------------------------------------------------
    def stop(self):
        
        print("Parado")
        self.pi.write(self.motorAOut, LOW)
        self.pi.write(self.motorAIn, LOW)
        self.pi.write(self.motorBIn, LOW)
        self.pi.write(self.motorBOut, LOW)

    #--------------------------------------------------------
    #--------------------------------------------------------
    def start(self, nFrequencia = 100, nDutyCircle = 64):

        PinsMotores = [self.motorAOut, self.motorAIn, self.motorBIn, self.motorBOut]
        self.pi = pigpio.pi()
        
        #Configura motor
        for A in PinsMotores:
            self.pi.set_mode(A, pigpio.OUTPUT)
            #Motor trabalha a 90RPM em 3V e 200RPM em 6V
            #90RPM = 1.5 Hz | 200RMP = 3.33Hz
            self.pi.set_PWM_frequency(A, nFrequencia)#Frequencia
            '''
            pi.set_PWM_dutycycle(4,   0) # PWM off
            pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
            pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
            pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
            pigpio.zip
            '''   
            self.pi.set_PWM_dutycycle(A, nDutyCircle)#ChangeDutyCycle


        self.pi.set_mode(self.encoderB, pigpio.INPUT)
        self.pi.set_mode(self.encoderA, pigpio.INPUT)

        self.pi.set_pull_up_down(self.encoderB, pigpio.PUD_UP)
        self.pi.set_pull_up_down(self.encoderA, pigpio.PUD_UP)

        self.callbackEsq = self.pi.callback(self.encoderB, pigpio.EITHER_EDGE, self.CalculaVoltaRotaEsquerda)
        self.callbackDir = self.pi.callback(self.encoderA, pigpio.EITHER_EDGE, self.CalculaVoltaRotaDireita)

    #--------------------------------------------------------
    #--------------------------------------------------------
    def restart(self, nFrequencia = 2, nDutyCircle = 70):

        PinsMotores = [self.motorAOut, self.motorAIn, self.motorBIn, self.motorBOut]
      
        ##GPIO.cleanup()
        #GPIO.setmode(GPIO.BCM)

        #Configura motor
        for A in PinsMotores:
            #Motor trabalha a 90RPM em 3V e 200RPM em 6V
            #90RPM = 1.5 Hz | 200RMP = 3.33Hz
            if( ( A % 2 ) == 0 ):
                self.pi.set_PWM_frequency(A, nFrequencia)#Frequencia
                '''
                pi.set_PWM_dutycycle(4,   0) # PWM off
                pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
                pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
                pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
                pigpio.zip
                '''   
                self.pi.set_PWM_dutycycle(nDutyCircle)#ChangeDutyCycle

    #--------------------------------------------------------
    # clean()
    #--------------------------------------------------------
    def clean(self):
        # This command clears the configuration from the GPIO interface
        self.callbackEsq.cancel()
        self.callbackDir.cancel()
        self.stop()
        self.pi.stop()
    #//    

    #--------------------------------------------------------
    # CalculaVolta()
    #--------------------------------------------------------
    def CalculaVoltaRotaDireita(self,porta,level, tick):

        #print(porta, level, tick)

        if( level == 1 ):
            print("#########################DIREITA#########################")
            self.RotacaoDir += 1
            if(self.RotacaoDir >= self.TotalVolta ):
                self.RotacaoDir = 0
            
    def CalculaVoltaRotaEsquerda(self,porta,level, tick):

        #print(porta, level, tick)

        if( level == 1):
            print("#########################ESQUERDA########################")
            self.RotacaoEsq += 1
            if( self.RotacaoEsq >= self.TotalVolta ):
                self.RotacaoEsq = 0


a = motores(24,23,17,22,26,19)
a.start(100,192)
a.frente(2)
a.clean()
del a
#//

