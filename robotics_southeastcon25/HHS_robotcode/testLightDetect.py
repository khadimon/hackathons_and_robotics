import RPi.GPIO as GPIO
from gpiozero import Button
from time import sleep
GPIO.setmode(GPIO.BCM)

#Setups for input pins
button = Button(22) #input pin for light detection module

#GPIO pin setup
#GPIO.setup(in1,GPIO.IN)

def startLightCheck():
    while !button.is_pressed: 
        sleep(0.1)





    
