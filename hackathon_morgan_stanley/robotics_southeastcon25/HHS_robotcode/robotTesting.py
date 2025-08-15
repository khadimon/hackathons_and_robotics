import RPi.GPIO as GPIO
from gpiozero import Button
from time import sleep
GPIO.setmode(GPIO.BCM)


# Setup for Pins


#Setups for input pins
button = Button(22) #input pin for light detection module


in1 = 2 #motor 1 input 1(pin 3)
in2 = 3 #motor 1 input 2(pin 5)
in3 = 5 #motor 2 input 1(pin 29)
in4 = 6 #motor 2 input 2 (pin 31)

in5 = 24 #motor 3 input 1 (pin 18)
in6 = 23 #motor 3 input 2 (pin 16)
in7 = 17 #motor 4 input 1 (pin 11)
in8 = 27 #motor 4 input 2 (pin 13)

in9 = 17 #motor 5 input1 (pin11)
in10 = 27 #motor 5 input 2 (pin 13)
in11 = 22 #motor6 input 1 (pin 15)
in12 = 23 #motor 6 input 2 (pin 16)



ENA = 12 #pwm for motor 1(pin 32)
ENA_B = 13 #pwm for motor 2(pin 33)
ENA_C = 18 #pwm for motor 3(pin 12)
ENA_D = 19 #pwm for motor 4 (pin 35)

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
# GPIO.setup(in11,GPIO.OUT)
# GPIO.setup(in12,GPIO.OUT)

#Enable pins 
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENA_B,GPIO.OUT)
GPIO.setup(ENA_C,GPIO.OUT)
GPIO.setup(ENA_D,GPIO.OUT)

# Setup for PWM for both motors
one_two = GPIO.PWM(ENA,1000) 
three_four = GPIO.PWM(ENA_B,1000)
five_six = GPIO.PWM(ENA_C, 1000)
seven_eight = GPIO.PWM(ENA_D, 1000)


# Doing Things Now

#GPIO.setup(in1,GPIO.IN)

def startLightCheck():
    while not button.is_pressed: 
        sleep(0.1)

def forward(speed, time):
    # left motor forward
    one_two.start(speed)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

    # right motor forward
    three_four.start(speed)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(time)
    
        # left motor off
    one_two.start(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    # right motor off
    three_four.start(0)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
def backward(speed, time):
    # left motor forward
    one_two.start(speed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

    # right motor forward
    three_four.start(speed)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(time)
    
        # left motor off
    one_two.start(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    # right motor off
    three_four.start(0)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
    
def leftpivot(speed, time):
    # left motor forward
    one_two.start(speed)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

    # right motor forward
    three_four.start(speed)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    
    
    # BACK wheel turn left
    
    five_six.start(speed)
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    sleep(time)
    
        # left motor off
    one_two.start(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    

    # right motor off
    three_four.start(0)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
    five_six.start(0)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    
def rightpivot(speed, time):
    # left motor forward
    one_two.start(speed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

    # right motor forward
    three_four.start(speed)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    
    
    # BACK wheel turn left
    
    five_six.start(speed)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)
    sleep(time)
    
        # left motor off
    one_two.start(0)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    

    # right motor off
    three_four.start(0)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
    five_six.start(0)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    
def scooping(speed, time):
   #SCOOP up
    seven_eight.start(speed)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)
    
    sleep(time)
    
    #SCOOP down
    seven_eight.start(speed)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)
    
    sleep(time)
    
    #motors off
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)


#motors off for motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


#Starting to do things

#checking for start light
startLightCheck()

print("Motors Moving Now...")

while True:
    forward(50,1.5)
    sleep(0.75)
    scooping(95,2)
    backward(52,1)
    leftpivot(56,1.6)





print("Motors Done Moving!") 