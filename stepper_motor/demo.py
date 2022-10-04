# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Simple test for using adafruit_motorkit with a stepper motor

from Jun: this is a working example that works with the motor
HAT board bought from Adafruit. The code drives the motor with
9V power source pretty well. No weird noise.
"""
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())

for i in range(10000):
    kit.stepper2.onestep(style=stepper.MICROSTEP)
    time.sleep(0.000001)

