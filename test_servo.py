import time
from adafruit_servokit import ServoKit

# initialize servokit
kit = ServoKit(channels=16)

# set (custom) range of the servo
kit.servo[3].set_pulse_width_range(500, 3000)

# reset to start
kit.servo[3].angle = 0
time.sleep(0.2)

# sweep to 180, then back to 0
kit.servo[3].angle = 180
time.sleep(0.8)
kit.servo[3].angle = 0
