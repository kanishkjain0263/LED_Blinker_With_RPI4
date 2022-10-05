import RPi.GPIO as GPIO   # To include the library so that we can use the raspberry pi GPIO pins in the code 
import time               # Importer this library to use the sleep method so that we can give a delay between the blinking of LED

GPIO.setwarnings(False)   # To ignore any warnings that the compiler gives and compiles the code
GPIO.setmode(GPIO.BOARD)  # For the numbering of GPIO pins of RPI
GPIO.setup(10, GPIO.OUT)  # Declaring the pin number 10 as output


try:                    
	while 1:  
		GPIO.output(10, GPIO.HIGH)    # To turn the LED on
		time.sleep(0.25)              # Delay so that the LED can be seen as blinking
		GPIO.output(10, GPIO.LOW)     # To turn the led off
		time.sleep(0.25)              
except KeyboardInterrupt:         # To stop the program if any interruption from the keyboard is detected
    GPIO.cleanup()                # To resset the ports that were used in the program so that the ports can be used again
    
    # Kanishk Jain
    # Task 5.1P - SIT210
    
