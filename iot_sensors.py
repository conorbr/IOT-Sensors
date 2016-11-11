
print ("  _       _                                          ")
print (" (_) ___ | |_     ___  ___ _ __  ___  ___  _ __ ___  ")
print (" | |/ _ \| __|   / __|/ _ \ '_ \/ __|/ _ \| '__/ __| ")
print (" | | (_) | |_    \__ \  __/ | | \__ \ (_) | |  \__ \ ")
print (" |_|\___/ \__|___|___/\___|_| |_|___/\___/|_|  |___/ ")
print ("            |_____|                                  ")
print (" ")
print (" /////////////////////////////////////////////////// ")
print (" ")


import grove_i2c_temp_hum_mini
import time

t= grove_i2c_temp_hum_mini.th02()
while True:
	print("Temp: %.2fC\tHumidity:%.2f" %(t.getTemperature(),t.getHumidity()),"%")
	time.sleep(.5)
