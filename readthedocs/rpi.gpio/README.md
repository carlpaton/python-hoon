### Servos

```python
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# There is another mode called `GPIO.BCM` for BCM pin numbering, not sure what this is?

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)

# Note 11 is the pi's pin, 50Hz pulse (analog servo), 300 would be for digital
servo = GPIO.PWM(11,50)

# Start PWM running, but with value of 0 (pulse off)
servo.start(0)

# duty is a percentage from 0 to 100 which allows for decimals like 3.33
# 2% = 0 degrees
# 7% = 90 degrees
# 12% = 180 degrees
# setting it then back to 0 stops the servo from jittering, just set `time.sleep(0.5)` before so you give the servo time to move to the position
duty = 2
servo.ChangeDutyCycle(duty)
servo.ChangeDutyCycle(0)

# Clean up
servo.stop()
GPIO.cleanup()
```

* https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

### LED

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.OUT)

# At 10Hz the LED will flicker
pwm = GPIO.PWM(25, 10)

# Frequency is now 50 Hz - LED stops flickering
pwm.ChangeFrequency(50)

print("5%")
pwm.ChangeDutyCycle(5)   # Duty cycle is now 5%

# Sleeper between duty ramp up
time.sleep(0.5)

print("100%")
pwm.ChangeDutyCycle(100) # Duty cycle is now 100%

# Clean up
pwm.stop()
GPIO.cleanup()
```

* [https://reviseomatic.org/help/x-Raspberry-Pi/RasPi%20GPIO-PWM.php](https://reviseomatic.org/help/x-Raspberry-Pi/RasPi GPIO-PWM.php)

