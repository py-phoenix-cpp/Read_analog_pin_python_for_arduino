import pyfirmata
import time

board = pyfirmata.Arduino('/dev/usbmodem1201')
# usbmodem1201 it's my Mac port
it = pyfirmata.util.Iterator(board)
it.start()

analog_input_value = board.get_pin('a:0:i')
# board.get_pin('a:0:i') a-> analog pin, 0-> analog A0 pin, i->INPUT
# analog_input_value -> it's variable

while True:
    analog_pin_value = analog_input_value.read()
    print(analog_pin_value)
    time.sleep(0.1)