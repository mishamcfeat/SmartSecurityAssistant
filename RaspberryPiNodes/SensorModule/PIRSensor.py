import RPi.GPIO as GPIO
import time

PIR_PIN = 17  # GPIO pin number for the PIR sensor


def initialise_pir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def read_pir():
    motion_detected = GPIO.input(PIR_PIN)
    if motion_detected:
        time.sleep(0.2)  # Short delay to filter out the noise
        motion_detected = GPIO.input(PIR_PIN)  # Read PIR sensor again
    return motion_detected


if __name__ == "__main__":
    try:
        initialise_pir()
        print("PIR Module Test (CTRL+C to exit)")
        time.sleep(2)  # Waiting for PIR to stabilize
        print("Ready")

        while True:
            print(read_pir())
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Quitting")
        GPIO.cleanup()