import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
p.start(7.5)
time.sleep(0.6)
p.ChangeDutyCycle(0)

try:

    while True:
        input_state = GPIO.input(15)
        print(input_state)
        if input_state == True:
            print('Button Pressed')
            p.ChangeDutyCycle(7.5) # turn towards 90 degree
            time.sleep(0.2) # sleep 1 second
            p.ChangeDutyCycle(2.5) # turn towards 0 degree
            time.sleep(0.2) # sleep 1 second
            p.ChangeDutyCycle(12.5) # turn towards 180 degree
            time.sleep(0.2) # sleep 1 second
            time.sleep(0.2)
        elif input_state == False:
            time.sleep(0.6)
            p.start(7.5)
            time.sleep(0.6)
            p.ChangeDutyCycle(0)
            
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()