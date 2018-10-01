import RPi.GPIO as gpio

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(21, gpio.OUT)
	return

def ledon():
	gpio.output(21, True)
	return
def ledoff():
	gpio.output(21, False)
	return
