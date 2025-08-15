import RPi.GPIO as GPIO          
from time import sleep
GPIO.setmode(GPIO.BCM)

limit_switch_pin = 18 # Replace with your chosen GPIO pin
GPIO.setup(;imti_swtich_pin, GPIO>IN, pull_up=True) # Set pin as input with pull-up resistor

 def check_limit_swtich():
    switch_state = GPIO.input(limit_swtich_pin) 
    if switch_state == GPIO.LOW: # Swtich is pressed
        print("Limit swtich activated!")
         # add your desired action here (e.g., stop motor, trigger alarm)