import time
import motorControl

#setup gpio
GPIO.setmode(GPIO.BOARD)

#create motor control
motors = motorControl.MotorController()

#go forward - both motors at 100%
motors.start(100)
time.sleep(2)

#go forward in a curve
# - motor A at 100%
# - motor B at 50%
motors.start(100,50)
time.sleep(2)

#go backward at 100%
# - using negative power
motors.start(-100)
time.sleep(2)

#stop
motors.stop()

#cleanup gpio
GPIO.cleanup()