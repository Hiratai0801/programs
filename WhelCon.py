import RPi.GPIO as GPIO
import sys


#GPIOセットアップ
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

#right
GPIO.output(5, GPIO.LOW)
GPIO.output(7, GPIO.HIGH)
#l
GPIO.output(13, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)
#c
GPIO.output(10, GPIO.LOW)
GPIO.output(12, GPIO.HIGH)

#PWMセットアップ
r = GPIO.PWM(3, 50)
l = GPIO.PWM(15, 50)
c = GPIO.PWM(8, 50)

r.start(0)
l.start(0)
c.start(0)

try:
    while True:
        k = sys.stdin.read(1)
        #[e]前進
        if k == 'e':
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(7, GPIO.LOW)
            r.ChangeDutyCycle(80)
            l.ChangeDutyCycle(80)
            c.ChangeDutyCycle(0)
        
        #[z]停止
        if k == 'z':
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            r.ChangeDutyCycle(0)
            l.ChangeDutyCycle(0)
            c.ChangeDutyCycle(0)
            
        #[x]全回転
        if k == 'x':
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            r.ChangeDutyCycle(80)
            l.ChangeDutyCycle(80)
            c.ChangeDutyCycle(80)

        #[f]終了
        if k == 'f':
            GPIO.output(13, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            r.ChangeDutyCycle(0)
            l.ChangeDutyCycle(0)
            c.ChangeDutyCycle(0)
            GPIO.cleanup()
            break

except KeyboardInterrupt:
    pass
