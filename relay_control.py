import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

relay_pins = [22, 27, 18, 17]  # GPIO pins for relays
GPIO.setup(relay_pins, GPIO.OUT, initial=GPIO.HIGH)

def toggle_relay(relay):
    GPIO.output(relay_pins[relay - 1], GPIO.LOW)
    sleep(1)  # Keep the relay on for 1 second
    GPIO.output(relay_pins[relay - 1], GPIO.HIGH)

if __name__ == '__main__':
    try:
        while True:
            relay = int(input("Enter relay number (1-4): "))
            if relay in [1, 2, 3, 4]:
                toggle_relay(relay)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
    except KeyboardInterrupt:
        GPIO.cleanup()

