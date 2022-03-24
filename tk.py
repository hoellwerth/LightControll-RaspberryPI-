import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Lichtsteuerung")
root.geometry("480x320")  # Configure the default height of the Window
root.resizable(width=True, height=True)  # if turned to false, the axis won't be resizable

photoon = ImageTk.PhotoImage(Image.open("assets/on.png"))  # the image to turn on the light
photooff = ImageTk.PhotoImage(Image.open("assets/off.png"))  # the image to turn off the light

GPIO.setmode(GPIO.BCM)
pin = 17  # the GPIO pin to trigger the relay
GPIO.setup(pin, GPIO.OUT)


def light1on():
    GPIO.output(pin, GPIO.HIGH)  # Turn on the light
    print("Light 1 On")  # logging


def light1off():
    GPIO.output(pin, GPIO.LOW)  # Turn off the light
    print("Light 1 off")  # logging


light1on = ttk.Button(root, image=photoon, padding=10, command=light1on)  # the button to turn on the light
light1on.pack(side="left")  # put the "on button" to the right side

light1off = ttk.Button(root, image=photooff, padding=10, command=light1off)  # the button to turn off the light
light1off.pack(side="right")  # put the "off button" to the right side

root.mainloop()
