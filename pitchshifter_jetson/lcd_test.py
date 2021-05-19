import time
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import board
import qwiic_twist
import sys
import os

def send2Pd(message=''):
	os.system("echo '" + message + "' | pdsend 3000")

def setup():

    #LCD Setup
    lcd_columns = 16
    lcd_rows = 2

    #GPIO Setup
    lcd_rs = digitalio.DigitalInOut(board.D26)
    lcd_en = digitalio.DigitalInOut(board.D19)
    lcd_d7 = digitalio.DigitalInOut(board.D27)
    lcd_d6 = digitalio.DigitalInOut(board.D22)
    lcd_d5 = digitalio.DigitalInOut(board.D24)
    lcd_d4 = digitalio.DigitalInOut(board.D25)
    lcd_backlight = digitalio.DigitalInOut(board.D4)

    #Initialize LCD
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    lcd.backlight = True

    # Print a two line message
    lcd.message = "Hello\nWorld"

    return lcd

def main(lcd):
    sleep(5)
    lcd.clear()

if __name__ == '__main__':
	try:
        lcd = setup()
		main(lcd)
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Script")
		sys.exit(0)