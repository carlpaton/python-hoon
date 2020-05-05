import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

print("Waiting for button push")
message = ""

while True:
    if GPIO.input(10) == GPIO.HIGH:
        message = "HIGH"
    elif GPIO.input(10) == GPIO.LOW:
       message = "LOW "
    
    print(message, end="\r", flush=True)