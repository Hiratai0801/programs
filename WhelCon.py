# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import jtalk

r = GPIO.PWM()
l = GPIO.PWM()
c = GPIO.PWM()

def setup():
    #GPIOセットアップ
    #GPIOピンの基盤の番号で指定する
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(基盤のピン番号, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    #GPIO.output(基盤のピン番号, GPIO.LOW)
    #GPIO.output(基盤のピン番号, GPIO.HIGH)
    #右ホイール
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    #左ホイール
    GPIO.output(13, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    #中央ホイール
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    #PWMセットアップ
    #変数 = GPIO.PWM(基盤のピン番号, デューティー比)
    r = GPIO.PWM(3, 50)
    l = GPIO.PWM(15, 50)
    c = GPIO.PWM(8, 50)
    #スタンバイOK
    #変数.start(出力値)
    r.start(0)
    l.start(0)
    c.start(0)

#直進処理
def straight():
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

#旋回処理
def turn():
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

#一時停止処理
def stop():
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

#会話終了時処理
def end():
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


def main():
    while True:
        f1 = open('word.txt', 'r', encoding='UTF-8')
        f2 = open('distance.txt', 'r', encoding='UTF-8')
        name =f1.read()
        dis = f2.read()
        if name == "person":
            if (dis <= 0.75) and (dis != 0.0):
                stop()
                jtalk.jtalk('とまりました')
            else:
                straight()
                jtalk.jtalk('ついていきますっ')
        elif name != "person":
            jtalk.jtalk('どこですかー？')
            turn()
            while True:
                name = f1.read()
                if name == "person":
                    jtalk.jtalk('見つけましたっ')
                    break

        
    
    

if __name__ == '__main__':

    main()