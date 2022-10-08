#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

# The number here is the physical number.
relayPin = 12    # define relayPin

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(relayPin, GPIO.OUT)   # set the relayPin to OUTPUT mode
    GPIO.output(relayPin, GPIO.LOW)  # make relayPin output LOW level 
    print ('using pin%d'%relayPin)

def loop():
    while True:
        GPIO.output(relayPin, GPIO.HIGH)  # make relayPin output HIGH level to turn on led
        print ('led turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(relayPin, GPIO.LOW)   # make relayPin output LOW level to turn off led
        print ('led turned off <<<')
        time.sleep(1)                   # Wait for 1 second

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

