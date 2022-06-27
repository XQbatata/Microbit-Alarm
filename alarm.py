'''
Example: Measure distance using Ultrasonic sensor and display results on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text


while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    p = pin1.read_digital()



    if distance_value < 400 and p == 1:
        pin2.write_digital(0)
        pin0.write_digital(1)
        pin16.write_analog(1023)
        initialize()
        clear_oled()
        sleep(1000)
        add_text(0, 0, "hello")
        add_text(0, 1, "fe")
        add_text(0, 2, "7rame")
        add_text(0, 3, "Qusay")
    elif: distance_value > 400 and p == 0:
        pin2.write_digital(1)
        pin0.write_digital(0)
        pin16.write_analog(0)
        initialize()
        clear_oled()
        sleep(1000)
        add_text(0, 0, "hello")
        add_text(0, 1, "ma fe")
        add_text(0, 2, "7rame")
        add_text(0, 3, "Qusay")