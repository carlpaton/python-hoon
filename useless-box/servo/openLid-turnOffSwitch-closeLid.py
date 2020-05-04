import RPi.GPIO as GPIO
import time

# Define duty in degrees
zeroDegrees = 2
ninetyDegrees = 7
oneHundredAndEightyDegrees = 14
sleep = 0.6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # Pin 12 for servo2

# Pulse off
servo1.start(0)
servo2.start(0)
time.sleep(sleep)

print ("Zero both")
servo1.ChangeDutyCycle(zeroDegrees)
servo2.ChangeDutyCycle(zeroDegrees)
time.sleep(sleep)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
time.sleep(sleep)

print ("Open lid")
servo1.ChangeDutyCycle(ninetyDegrees)
time.sleep(sleep)
servo1.ChangeDutyCycle(0)
time.sleep(sleep)

print ("Turn off the switch")
servo2.ChangeDutyCycle(oneHundredAndEightyDegrees)
time.sleep(sleep)
servo2.ChangeDutyCycle(0)
time.sleep(sleep)

print ("Pull switch arm back")
servo2.ChangeDutyCycle(zeroDegrees)
time.sleep(sleep)
servo2.ChangeDutyCycle(0)
time.sleep(sleep)

print ("Close lid")
servo1.ChangeDutyCycle(zeroDegrees)
time.sleep(sleep)
servo1.ChangeDutyCycle(0)
time.sleep(sleep)


#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()
print ("DONE")