import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import ttk
from PIL import Image, ImageTk
from os import *
import os

root = tk.Tk()
root.title("Lichtsteuerung")
root.geometry("480x320")
root.resizable(width=True, height=True)

photoon = ImageTk.PhotoImage(Image.open("assets/on.png"))
photooff = ImageTk.PhotoImage(Image.open("assets/off.png"))

GPIO.setmode(GPIO.BCM)
pin = 17
GPIO.setup(pin, GPIO.OUT)


def light1on():
    GPIO.output(pin, GPIO.HIGH)
    print("Light 1 On")


def light1off():
    GPIO.output(pin, GPIO.LOW)
    print("Light 1 off")


light1on = ttk.Button(root, image=photoon, padding=10, command=light1on)
light1on.pack(side="left")

light1off = ttk.Button(root, image=photooff, padding=10, command=light1off)
light1off.pack(side="right")

root.mainloop()
