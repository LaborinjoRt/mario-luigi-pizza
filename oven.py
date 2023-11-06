import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

#Setting pins to constants
DHTPIN = 12  # digital pin
BUTTON1 = 9
BUTTON2 = 8
REDLED = 4
GREENLED = 5
BUZZER = 3
STARTBUTTON = 8
state1 = False
state2 = False

#setup function where i set board,and initializing pin functions.
def setup():
    global board
    board = CustomTelemetrix()
    board.displayOn()
    board.set_pin_mode_digital_input_pullup(BUTTON1)
    board.set_pin_mode_digital_input_pullup(BUTTON2)
    board.set_pin_mode_digital_output(BUZZER)
    board.set_pin_mode_digital_output(REDLED)
    board.set_pin_mode_digital_output(GREENLED)
    board.set_pin_mode_dht(DHTPIN)
    board.set_pin_mode_digital_input_pullup(STARTBUTTON)

#loop where it actually displays data to Display
def loop():
    #put order variable just to test if it actually displays it.
    order = "12"
    #using these states, and levels to make button changes, and to make sure that both buttons work.
    global state1, state2
    button_pressed = board.digital_read(BUTTON1)
    level = button_pressed[0]

    button_pressed2 = board.digital_read(BUTTON2)
    level2 = button_pressed2[0]
    #Here it activates the countdown when i click button1
    if level == 0:
        state1 = True
        if state1:
            #The actual countdown loop, turns on red led light.
            countdown = 5
            while countdown >= 0:
                board.digital_write(REDLED, 1)
                print(countdown)
                board.displayShow(countdown)
                time.sleep(1)
                countdown -= 1
                board.digital_write(REDLED, 0)
            #loop finishes and turns off redled and below it turns on green led and buzzes
            print("Your order is ready!")
            board.digital_write(GREENLED, 1)
            board.analog_write(BUZZER, 4)
            time.sleep(0.15)
            board.analog_write(BUZZER, 0)
            time.sleep(0.15)
            board.analog_write(BUZZER, 4)
            time.sleep(0.15)
            board.analog_write(BUZZER, 0)
            #time.sleep(5)
            board.displayShow(order)
    #When i click button2 it "Resets" the display and turns off green led.
    if level2 == 0:
        state2 = True 
        board.digital_write(GREENLED, 0)

#This is just the default code to actually use the loops, etc.        
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)