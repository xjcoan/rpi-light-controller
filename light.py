import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

for i in range (0, 10):
	GPIO.output(4, True)
	GPIO.output(23, False)
	GPIO.output(17, True)
	GPIO.output(25, False)
	time.sleep(1)
	GPIO.output(25, True)
	GPIO.output(17, False)
	GPIO.output(4,False)
	GPIO.output(23, True)
	time.sleep(1)
	GPIO.output(23, False)
	GPIO.output(25, False)
