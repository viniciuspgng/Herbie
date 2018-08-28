import time
import pigpio


MOTOR_A1 = 23
MOTOR_A2 = 24

pi= pigpio.pi()

pi.set_PWM_frequency(MOTOR_A2, 100)

pi.set_servo_pulsewidth(MOTOR_A1, 0)
pi.set_PWM_dutycycle(MOTOR_A2,64)
time.sleep(3)

pi.stop()
