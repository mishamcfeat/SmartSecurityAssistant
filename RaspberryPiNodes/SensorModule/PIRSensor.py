import RPi.GPIO as GPIO

PIR_PIN = 17  # GPIO pin number for the PIR sensor

def initialize_pir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)

def read_pir():
    return GPIO.input(PIR_PIN)