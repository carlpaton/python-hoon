### Pi Resources

Move this here - https://carlpaton.github.io/2019/12/pi-resources/

Re-install file manager when it crashes on start.

```
sudo apt-get install --reinstall pcmanfm
```

### GPIO

```py
pinout
```

### Switches

Determine if switches are on (high) or off (low)

* https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

### Servo Motor Control

A servo allows precise control of the angular position of its shaft.
Standard servos accept 4.6 to 6 volts.

Yellow/White = Control signal
Red = positive power lead
Black/Brown = negative power lead

#### Control signal

This needs to be a `pulse width modulation (PWM)` square wave.
The square wave needs to be 50 herts (so a pulse of every 0.2 seconds)
The angle of the servo is controled by the length of the positive pulse (duty cycle)
The longer the pulse/period of the wave/duty cycle the larger the angle the servo will turn to and try hold itself at.

These values vary by servo but the degrees can be calculated as:
```
2% duty cycle = 0 degrees
12% duty cycle = 180 degrees
```

* https://www.youtube.com/watch?v=xHDT4CwjUQE

### Inside the Useless Machine

* https://www.youtube.com/watch?v=PRn1Uzp54uw