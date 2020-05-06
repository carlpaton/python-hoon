import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

zeroDegrees = 2
ninetyDegrees = 7
oneHundredAndEightyDegrees = 14
sleep3 = 0.6 # 3 seconds
sleep2 = 0.4 # 2 seconds
sleep1 = 0.2 # 1 second

p = GPIO.PWM(18, 50)
p.start(zeroDegrees)
time.sleep(sleep3)
p.ChangeDutyCycle(0)
zero_servo = False

try:

    while True:
        input_state = GPIO.input(15)
        if input_state == True:
            
            print('Human put the switch on')
            #90
            p.ChangeDutyCycle(ninetyDegrees)
            time.sleep(sleep2)
            p.ChangeDutyCycle(0)
            #180
            p.ChangeDutyCycle(oneHundredAndEightyDegrees)
            time.sleep(sleep2)
            p.ChangeDutyCycle(0)
            #0
            p.ChangeDutyCycle(zeroDegrees)
            time.sleep(sleep3)
            p.ChangeDutyCycle(0)
            zero_servo = True
            
        elif input_state == False:
            
            if zero_servo == True:
                
                print('Box turned it off')
                p.start(zeroDegrees)
                time.sleep(sleep3)
                p.ChangeDutyCycle(0)
                zero_servo = False
            
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()