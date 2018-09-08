import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 18    
in_1_pin = 23
in_2_pin = 24

enable_pin1 = 16    
in_3_pin = 20
in_4_pin = 21

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in_1_pin, GPIO.OUT)
GPIO.setup(in_2_pin, GPIO.OUT)

GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(in_3_pin, GPIO.OUT)
GPIO.setup(in_4_pin, GPIO.OUT)

motor_pwm  = GPIO.PWM(enable_pin, 500)
motor_pwm1 = GPIO.PWM(enable_pin1, 500)
motor_pwm.start(0)
motor_pwm1.start(0)

def forward(duty):
        
    motor_pwm.ChangeDutyCycle(duty)    
    motor_pwm1.ChangeDutyCycle(duty)
    #Esquerdo
    GPIO.output(in_1_pin, True) 
    GPIO.output(in_2_pin, False)
    #Direito    
    GPIO.output(in_3_pin, True) 
    GPIO.output(in_4_pin, False)
    
def reverse(duty):

    motor_pwm.ChangeDutyCycle(duty)
    motor_pwm1.ChangeDutyCycle(duty)
    #Esquerdo
    GPIO.output(in_1_pin, False) 
    GPIO.output(in_2_pin, True)
    #Direito    
    GPIO.output(in_3_pin, False) 
    GPIO.output(in_4_pin, True) 
  
def stop():
    
    motor_pwm.ChangeDutyCycle(0)
    motor_pwm1.ChangeDutyCycle(0)
    #Esquerdo
    GPIO.output(in_1_pin, False) 
    GPIO.output(in_2_pin, False)
    #Direito    
    GPIO.output(in_3_pin, False) 
    GPIO.output(in_4_pin, False) 
    
try:         
    while True:        
        direction = input('Enter direction letter (f - forward, r - reverse, s - stop): ')
        if direction[0] == 's':
            stop()
        else:
            duty = input('Enter Duty Cycle (0 to 100): ')
            if direction[0] == 'f':
                forward(int(duty))
            elif direction[0] == 'r':
                reverse(int(duty))
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()
