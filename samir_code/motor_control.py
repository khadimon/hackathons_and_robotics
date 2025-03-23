import RPi.GPIO as GPIO
import time
from gpiozero import Button  # New import for light sensor detection

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# --- Pin Definitions ---
# Drive Motors (H Bridge)
motorLeftIn1  = 4
motorLeftIn2  = 5
motorLeftEn   = 8   # PWM
motorRightIn1 = 6
motorRightIn2 = 7
motorRightEn  = 9   # PWM

# Pickup Motor
pickupIn1 = 10
pickupIn2 = 11
pickupEn  = 12   # PWM

# Conveyor Motor
# Note: Raspberry Pi does not have analog pins, so choose appropriate BCM pins.
conveyorIn1 = 13
conveyorIn2 = 14  # replacing A0 with BCM 14
conveyorEn  = 15  # replacing A1 with BCM 15

# --- Setup GPIO Pins ---
drive_pins = [motorLeftIn1, motorLeftIn2, motorRightIn1, motorRightIn2]
other_pins = [pickupIn1, pickupIn2, conveyorIn1, conveyorIn2]
for pin in drive_pins + other_pins:
    GPIO.setup(pin, GPIO.OUT)

# Create PWM objects
pwmMotorLeft = GPIO.PWM(motorLeftEn, 1000)    # 1000 Hz for drive motors
pwmMotorRight = GPIO.PWM(motorRightEn, 1000)
pwmPickup = GPIO.PWM(pickupEn, 1000)            # 1000 Hz for pickup
pwmConveyor = GPIO.PWM(conveyorEn, 1000)         # 1000 Hz for conveyor

# Start PWM (0% duty cycle for drive motors)
pwmMotorLeft.start(0)
pwmMotorRight.start(0)
# Run pickup and conveyor initially at their default speeds:
pwmPickup.start(75)
pwmConveyor.start(25)

def pickup():
    GPIO.output(pickupIn1, GPIO.HIGH)
    GPIO.output(pickupIn2, GPIO.LOW)

# --- Motor Control Functions ---
def drive_forward(duration):
    GPIO.output(motorLeftIn1, GPIO.HIGH)
    GPIO.output(motorLeftIn2, GPIO.LOW)
    GPIO.output(motorRightIn1, GPIO.HIGH)
    GPIO.output(motorRightIn2, GPIO.LOW)
    pwmMotorLeft.ChangeDutyCycle(59)
    pwmMotorRight.ChangeDutyCycle(59)
    time.sleep(duration)

def drive_backward(duration):
    GPIO.output(motorLeftIn1, GPIO.LOW)
    GPIO.output(motorLeftIn2, GPIO.HIGH)
    GPIO.output(motorRightIn1, GPIO.LOW)
    GPIO.output(motorRightIn2, GPIO.HIGH)
    pwmMotorLeft.ChangeDutyCycle(59)
    pwmMotorRight.ChangeDutyCycle(59)
    time.sleep(duration)

def turn_right(duration):
    GPIO.output(motorLeftIn1, GPIO.HIGH)
    GPIO.output(motorLeftIn2, GPIO.LOW)
    GPIO.output(motorRightIn1, GPIO.LOW)
    GPIO.output(motorRightIn2, GPIO.HIGH)
    pwmMotorLeft.ChangeDutyCycle(59)
    pwmMotorRight.ChangeDutyCycle(59)
    time.sleep(duration)

def turn_left(duration):
    GPIO.output(motorLeftIn1, GPIO.LOW)
    GPIO.output(motorLeftIn2, GPIO.HIGH)
    GPIO.output(motorRightIn1, GPIO.HIGH)
    GPIO.output(motorRightIn2, GPIO.LOW)
    pwmMotorLeft.ChangeDutyCycle(59)
    pwmMotorRight.ChangeDutyCycle(59)
    time.sleep(duration)

def stop_motors(duration):
    pwmMotorLeft.ChangeDutyCycle(0)
    pwmMotorRight.ChangeDutyCycle(0)
    time.sleep(duration)

# --- New Movement Helper ---
def move_robot_based_on_direction(direction):
    if direction == "left":
        turn_left(0.5)
        drive_forward(2)
    elif direction == "right":
        turn_right(0.5)
        drive_forward(2)
    elif direction == "center":
        drive_forward(2)
    else:
        stop_motors(0.3)

# --- New Path Movement Function ---
def move_along_path(path):
    for i in range(1, len(path)):
        prev = path[i-1]
        curr = path[i]
        di = curr[0] - prev[0]
        dj = curr[1] - prev[1]
        if di == 1:
            drive_forward(2)
        elif di == -1:
            drive_backward(2)
        elif dj == 1:
            turn_right(0.5)
            drive_forward(2)
        elif dj == -1:
            turn_left(0.5)
            drive_forward(2)
        else:
            stop_motors(0.3)

# --- New Functions to run Pickup and Conveyor ---
def run_conveyor(duration):
    # Set conveyor to run at 25% power for the given duration.
    GPIO.output(conveyorIn1, GPIO.HIGH)
    GPIO.output(conveyorIn2, GPIO.HIGH)
    pwmConveyor.ChangeDutyCycle(25)
    time.sleep(duration)
    pwmConveyor.ChangeDutyCycle(0)

def run_pickup(duration):
    # Set pickup motor to run at 75% power for the given duration.
    GPIO.output(pickupIn1, GPIO.HIGH)
    GPIO.output(pickupIn2, GPIO.LOW)
    pwmPickup.ChangeDutyCycle(75)
    time.sleep(duration)
    pwmPickup.ChangeDutyCycle(0)

# --- Main Sequence ---
def main():
    # Wait for light sensor activation before starting
    light_sensor = Button(22)
    print("Waiting for light sensor activation...")
    light_sensor.wait_for_press()
    print("Light sensor activated. Starting robot operation.")
    # Start driving the robot forward for 2 seconds.
    run_pickup(180)
    drive_forward(2)
    turn_right(0.5)
    drive_forward(2)
    turn_left(0.5)
    # Stop the motors for 0.3 seconds.
    stop_motors(0.3)
    drive_backward(2)
    turn_left(0.5)
    drive_forward(2)
    stop_motors()
    # Run the conveyor for 2 seconds at 25% power.
    run_conveyor(2)

    # Cleanup PWM objects and GPIO settings
    pwmMotorLeft.stop()
    pwmMotorRight.stop()
    pwmPickup.stop()
    pwmConveyor.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()