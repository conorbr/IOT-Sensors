
print ("  _       _                                          ")
print (" (_) ___ | |_     ___  ___ _ __  ___  ___  _ __ ___  ")
print (" | |/ _ \| __|   / __|/ _ \ '_ \/ __|/ _ \| '__/ __| ")
print (" | | (_) | |_    \__ \  __/ | | \__ \ (_) | |  \__ \ ")
print (" |_|\___/ \__|___|___/\___|_| |_|___/\___/|_|  |___/ ")
print ("            |_____|                                  ")
print (" ")
print (" /////////////////////////////////////////////////// ")
print (" ")


import time
import grovepi

# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND
loudness_sensor = 1

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(loudness_sensor)

        print("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")
