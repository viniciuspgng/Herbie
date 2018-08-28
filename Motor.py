###import time
import pigpio

LOW = 0
HIGH = 1

class motores:

    motorAIn = 24 #pino 18
    motorAOut = 23 #pino 16
    motorBIn = 17 #pino 11
    motorBOut = 22 #pino 15

    motorEnbA = 6  #pino 31
    motorEnbB = 13 #pino 33
    
    #Encoder de 20 faixas
    encoderA = 26 #pino 37
    encoderB = 19 #pino 35

    callbackEsq = None
    callbackDir = None
    RotacaoDir = 0
    RotacaoEsq = 0
    TotalVolta = 10
    QdtVoltasDir = 0
    QdtVoltasEsq = 0
    pos = 0
    pi = None#pigpio.pi()

      
    # define which pins we are driving the L298N with

    #motorAOut = 17 #pino 11
    #motorAIn = 22 #pino 15
    #motorBIn = 24 #pino 18
    #motorBOut = 23 #pino 16
    def __init__(self, pmotorAIn=None, pmotorAOut=None, pmotorBIn=None, pmotorBOut=None, pencoderA=None, pencoderB=None, pmotorEnbA=None, pmotorEnbB=None ):
        self.pi = pigpio.pi()
        self.motorAIn  = (self.motorAIn  if (pmotorAIn == None)  else pmotorAIn)
        self.motorAOut = (self.motorAIn  if (pmotorAOut == None) else pmotorAOut)
        self.motorBIn  = (self.motorBIn  if (pmotorBIn == None)  else pmotorBIn)
        self.motorBOut = (self.motorBOut if (pmotorBOut == None) else pmotorBOut)
        self.encoderA  = (self.encoderA  if (pencoderA == None)  else pencoderA)
        self.encoderB  = (self.encoderB  if (pencoderB == None)  else pencoderB)
        self.motorEnbA = (self.motorEnbA  if (pmotorEnbA == None)  else pmotorEnbA)
        self.motorEnbB = (self.motorEnbB  if (pmotorEnbB == None)  else pmotorEnbB)

    #--------------------------------------------------------
    # frente()
    #--------------------------------------------------------
    def frente(self, qtdrodar ):
        qtdDir = 0
        qtdEsq = 0
        voltas = qtdrodar*self.TotalVolta
        #print("para Frente")
        self.RotacaoDir = 0
        self.RotacaoEsq = 0

        '''while (voltas >= (self.RotacaoDir/self.TotalVolta) and voltas >= (self.RotacaoEsq/self.TotalVolta)):
            if (self.RotacaoDir < self.RotacaoEsq ):#direita
                self.pi.write(self.motorAIn, HIGH)
                self.pi.write(self.motorAOut, LOW)
                qtdDir = qtdDir +1

            elif (self.RotacaoEsq < self.RotacaoDir):#esquerda
                self.pi.write(self.motorBIn, HIGH)
                self.pi.write(self.motorBOut, LOW)
                
                qtdEsq = qtdEsq +1

            elif (self.RotacaoEsq == self.RotacaoDir):#ambos
                self.pi.write(self.motorAIn, HIGH)
                self.pi.write(self.motorAOut, LOW)
                self.pi.write(self.motorBIn, HIGH)
                self.pi.write(self.motorBOut, LOW)
                qtdDir = qtdDir +1
                qtdEsq = qtdEsq +1
            #$time.sleep(0.35)
         '''
        self.pi.write(self.motorAIn, HIGH)
        self.pi.write(self.motorAOut, LOW)
        self.pi.write(self.motorBIn, HIGH)
        self.pi.write(self.motorBOut, LOW)
        ###time.sleep(qtdrodar)
        self.stop()
            
            #print("qtdDir", str(qtdDir))
            #print("qtdEsq", str(qtdEsq))
            #print("Rotacao esq", str(self.RotacaoEsq))
            #print("Rotacao dir", str(self.RotacaoDir))

    #--------------------------------------------------------
    # frenteEsq()
    #--------------------------------------------------------
    def frenteEsq( self,qtdrodar=0.1 ):
        
        print("para esquerda")
        '''
        voltas = qtdrodar*self.TotalVolta
        self.RotacaoDir = 0
        self.RotacaoEsq = 0

        while (voltas >= (self.RotacaoDir/self.TotalVolta) and qtdrodar >= (self.RotacaoEsq/self.TotalVolta)):
            self.pi.write(self.motorBIn, HIGH)
            self.pi.write(self.motorBOut, LOW)
        '''
        self.pi.write(self.motorBIn, HIGH)
        self.pi.write(self.motorBOut, LOW)
        ###time.sleep(qtdrodar)
        self.stop()
    #--------------------------------------------------------
    # frenteDir()
    #--------------------------------------------------------
    def frenteDir( self,qtdrodar):
        
        print("para direita")
        '''voltas = qtdrodar*self.TotalVolta
        self.RotacaoDir = 0
        self.RotacaoEsq = 0

        while (voltas >= (self.RotacaoDir/self.TotalVolta) and qtdrodar >= (self.RotacaoEsq/self.TotalVolta)):
            self.pi.write(self.motorAIn, HIGH)
            self.pi.write(self.motorAOut, LOW)'''

        self.pi.write(self.motorAIn, HIGH)
        self.pi.write(self.motorAOut, LOW)
        ###time.sleep(qtdrodar)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def reh(self, tempo=0.1):
        
        print("para tras")
        '''
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
            self.pi.write(self.motorBOut, HIGH)'''

        self.pi.write(self.motorAIn, LOW)
        self.pi.write(self.motorAOut, HIGH)
        self.pi.write(self.motorBIn, LOW)
        self.pi.write(self.motorBOut, HIGH)
        ###time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def rehDir(self,tempo =0.1):
        
        print("re para direita")
        self.pi.write(self.motorAIn, LOW)
        self.pi.write(self.motorAOut, HIGH)

        ###time.sleep(tempo)
        self.stop()
    #--------------------------------------------------------
    #--------------------------------------------------------
    def rehEsq(tempo = 0.1):
        
        print("re para tras esquerda ")
        self.pi.write(self.motorAOut, LOW)
        self.pi.write(self.motorAIn, HIGH)

        ###time.sleep(tempo)
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
    def start(self, nFreqMotorA = 100, nDutyMotorA = 64, nFreqMotorB = 100, nDutyMotorB = 64):

        PinsMotores = [self.motorAOut, self.motorAIn, self.motorBIn, self.motorBOut, self.motorEnbA, self.motorEnbB]
      
        #Configura motor
        for A in PinsMotores:
            self.pi.set_mode(A, pigpio.OUTPUT)
            #Motor trabalha a 90RPM em 3V e 200RPM em 6V
            #90RPM = 1.5 Hz | 200RMP = 3.33Hz
            print("porta: ",str(A))
            if( A == self.motorEnbA):
                print("frequency: ", str(self.pi.set_PWM_frequency(A, nFreqMotorA)))#Frequencia
                print("Duty : ", str(self.pi.set_PWM_dutycycle(A, nDutyMotorA)))#ChangeDutyCycle
            elif(A == self.motorEnbB):
                print("frequency: ", str(self.pi.set_PWM_frequency(A, nFreqMotorB)))#Frequencia
                print("Duty : ", str(self.pi.set_PWM_dutycycle(A, nDutyMotorB)))#ChangeDutyCycle
            '''
            pi.set_PWM_dutycycle(4,   0) # PWM off
            pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
            pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
            pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
            pigpio.zip
            ''' 


        self.pi.set_mode(self.encoderB, pigpio.INPUT)
        self.pi.set_mode(self.encoderA, pigpio.INPUT)

        self.pi.set_pull_up_down(self.encoderB, pigpio.PUD_UP)
        self.pi.set_pull_up_down(self.encoderA, pigpio.PUD_UP)

        self.callbackEsq = self.pi.callback(self.encoderB, pigpio.FALLING_EDGE, self.CalculaVoltaRotaEsquerda)
        self.callbackDir = self.pi.callback(self.encoderA, pigpio.FALLING_EDGE, self.CalculaVoltaRotaDireita)

    #--------------------------------------------------------
    #--------------------------------------------------------
    def restart(self, nDutyCircle = 70,nFrequencia = 50):

        PinsMotores = [self.motorAOut, self.motorAIn, self.motorBIn, self.motorBOut]
      
        ##GPIO.cleanup()
        #GPIO.setmode(GPIO.BCM)

        #Configura motor
        for A in PinsMotores:
            #Motor trabalha a 90RPM em 3V e 200RPM em 6V
            #90RPM = 1.5 Hz | 200RMP = 3.33Hz
            #if( ( A % 2 ) == 0 ):
            self.pi.set_PWM_dutycycle(A, nDutyCircle)#ChangeDutyCycle
            self.pi.set_PWM_frequency(A, nFrequencia)#Frequencia
            
            #$time.sleep(1)
            '''
            pi.set_PWM_dutycycle(4,   0) # PWM off
            pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
            pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
            pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
            pigpio.zip
            '''   
            

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
            #print("#########################DIREITA#########################")
            self.RotacaoDir = self.RotacaoDir + 1
            if(self.RotacaoDir == self.TotalVolta ):
                self.QdtVoltasDir = self.QdtVoltasDir + 1 
        print("levelDireita", str(level))
        
    def CalculaVoltaRotaEsquerda(self,porta,level, tick):

        #print(porta, level, tick)

        if( level == 1):
            #print("#########################ESQUERDA########################")
            self.RotacaoEsq += 1
            if( self.RotacaoEsq == self.TotalVolta ):
                self.QdtVoltasEsq = self.QdtVoltasEsq + 1
        print("levelEsquerda", str(level))
'''
a = motores(24,23,17,22,26,19,6,13)


a.clean()
'''
