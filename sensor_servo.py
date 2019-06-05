import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685
from adafruit_servokit import ServoKit

# initialize servokit
kit = ServoKit(channels=16)
# set range
kit.servo[3].set_pulse_width_range(500, 3000)

TRIG = 23 
ECHO = 24

def measure():
    # This function measures a distance
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    stop = 0

    while GPIO.input(ECHO)==0:
        start = time.time()

    while GPIO.input(ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

# sweeps the servo 0 -> 180 -> 0
def sweep():
    # reset servo angle to 0
    kit.servo[3].angle = 0
    time.sleep(0.2)

    # sweep 180 -> 0
    kit.servo[3].angle = 180
    time.sleep(0.8)
    kit.servo[3].angle = 0
    time.sleep(0.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

try:
    # keep measuring distances
    print("Starting Distance Measurements")
    while True:
        num_measurements = 3
        distance = 0

        for _ in range(num_measurements):
            distance += measure()
            time.sleep(0.1)

        distance /= num_measurements

        print("Measured average:", distance, "cm")

        # sweep if close
        if distance <= 5:
            print('Sweeping')
            sweep()

except KeyboardInterrupt:
    GPIO.cleanup()
