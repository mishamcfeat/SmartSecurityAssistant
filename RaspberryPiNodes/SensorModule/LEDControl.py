import RPi.GPIO as GPIO

LED_PIN = 27  # GPIO pin number for the IR LED

def initialize_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)