# print out a message what's going to happen 
print("Starting initialisation for uLCD...")

# import the needed extensions for python
import serial
import time
from time import sleep
import sys

# open the serial connection (check with dmesg if it's not working)
ser = serial.Serial('/dev/ttyUSB0', 9600)

# check the connection
if ser.isOpen() == True:
    print("connection ok")
else:
    print("connection failed")
    print("exiting...")
    sys.exit()

# write the command for AUTOBAUD by sending the character 'U'
ser.write(b'U')
sleep(1)

# write the command for ERASE by sending the character 'E'
ser.write(b'E')
sleep(1)

# write the welcome screen
# Byte 1: column = 0
# Byte 2: row = 0
# Byte 3: font = 0
# Byte 4 & 5: color = ffff
# Byte 5+: "string"
# Byte n: terminator = 0
ser.write(b's\x00\x00\x03\xff\xffpy-uLCD\x00')
sleep(0.08)
ser.write(b's\x00\x07\x00\xff\xffLicense:        GNU GPLv3\x00')
sleep(0.08)
ser.write(b's\x00\x08\x00\xff\xffDeveloper:      nino.ninux@gmail.com\x00')
sleep(0.08)
ser.write(b's\x00\x09\x00\xff\xffOrganisation:   ACCEFA - Team 39\x00')
sleep(0.08)
ser.write(b's\x00\x0A\x00\xff\xffDevice:         4D Systems uLCD32-PT\x00')
sleep(0.08)
ser.write(b's\x00\x0B\x00\xff\xffBaud Rate:      9600\x00')
sleep(0.08)
ser.write(b's\x00\x0C\x00\xff\xffParity:         No\x00')
sleep(0.08)

ser.close()
# write out a message that the sequence is done
print("Initialisation for uLCD is done.")
