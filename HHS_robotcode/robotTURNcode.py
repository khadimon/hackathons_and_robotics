import RPi.GPIO as GPIO          
from time import sleep
GPIO.setmode(GPIO.BCM)


# Setup for Pins
in1 = 2 #motor 1 input 1(pin 3)
in2 = 3 #motor 1 input 2(pin 5)
in3 = 5 #motor 2 input 1(pin 29)
in4 = 6 #motor 2 input 2 (pin 31)

in5 = 4 #motor 3 input 1 (pin 22)
in6 = 8 #motor 3 input 2 (pin 24)
in7 = 1 #motor 4 input 1 (pin 28)
in8 = 9 #motor 4 input 2 (pin 21)

in9 = 17 #motor 5 input1 (pin11)
in10 = 27 #motor 5 input 2 (pin 13)
in11 = 22 #motor6 input 1 (pin 15)
in12 = 23 #motor 6 input 2 (pin 16)



ENA = 12 #pwm for motor 1(pin 32)
ENA_B = 13 #pwm for motor 2(pin 33)

#Pins for limit switches






#Outputs for motor 1
GPIO.setup(in1,GPIO.OUT) 
GPIO.setup(in2,GPIO.OUT)

#Outputs for motor 2
GPIO.setup(in3,GPIO.OUT) 
GPIO.setup(in4,GPIO.OUT)

#Outputs for motor 3
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)

#Outputs for motor 4
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)

#Outputs for motor 5
GPIO.setup(in9,GPIO.OUT)
GPIO.setup(in10,GPIO.OUT)

#Outputs for motor 6
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)

#Enable pins 
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENA_B,GPIO.OUT)

# Setup for PWM for both motors
one_two = GPIO.PWM(ENA,1000) 
three_four = GPIO.PWM(ENA_B,1000)


# Doing Things Now

#motors off for motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


one_two.start(100)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)


three_four.start(100)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
print("Motors Moving Now...") 

sleep(5)

print("Motors Done Moving!") 

