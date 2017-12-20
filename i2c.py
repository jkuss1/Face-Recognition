from os import system
from time import sleep

# Display Used: Newhaven NHD-0216K3Z-FL-GBW-V3
# May not work with other displays.

# Displays a message on LCD display using I2C.
def display_msg(text=""):
	sleep(1)

	# Clears LCD display.
	system("i2cset -y 1 0x28 0xFE 0x51")

	hex1 = ""
	hex2 = ""

	# Splits text variable to fit to LCD display
	# size of 2x16. Any characters over length of
	# 32 are dropped.
	text1 = text[0:16]
	text2 = text[16:32]

	# Converts each character in text variable (string)
	# to its decimal equivalent and saves them to a new
	# string.
	for char in text1:
		hex1 = hex1 + str(ord(char)) + " "

	for char in text2:
		hex2 = hex2 + str(ord(char)) + " "

	sleep(0.1)

	# Uses system command i2cset to write message to
	# LCD display.
	if len(text) == 1:
		system("i2cset -y 1 0x28 " + hex1)
	else:
		system("i2cset -y 1 0x28 " + hex1 + "0xFE 0x45 0x40 i")
		sleep(0.1)

		if hex2:
			system("i2cset -y 1 0x28 " + hex2 + "i")
