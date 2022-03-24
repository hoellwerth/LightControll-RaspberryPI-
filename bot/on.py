import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 17
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
print('debug')