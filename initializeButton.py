import RPi.GPIO as GPIO
import time
import os
from subprocess import Popen, PIPE

GPIO.setmode(GPIO.BCM)
button = 21

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	#If button is pressed execute run.sh
	if GPIO.input(button) == False:
		time.sleep(.5)
		output = Popen(["sh", "run.sh", ], stdout=PIPE).communicate()[0]
		print(output)
