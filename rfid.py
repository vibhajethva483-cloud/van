# Practical :
# Aim: Accessing RFID with Raspberry Pi.
# Hardware Requirements
# Raspberry Pi 
# RFID EM 18 Module
# MicroSD card with Raspberry Pi OS installed
# Power supply for Raspberry Pi
# Jumper wires (female-to-female as needed)
# Monitor, keyboard, mouse (for setup)

# Software Requirements
# Raspberry Pi OS installed and running
# Python 3  
# Circuit Connections:

#  Board Pin - Physical PIN Number - GPIO Number 
# TX-10-GPIO 15
# VCC-2-5 V
# GND-6-GROUND

#  Commands:
(disable login shell over serial, enable serial hardware)
sudo raspi-config  - # for configuring interface I2C
reboot
sudo apt-get update
sudo apt-get upgrade
pip3 install pyserial

To find your card_Id:
import serial
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
print("Scan your card...")
while True:
    data = ser.read(12)
    if data:
        print(data.decode('utf-8').strip())

Source Code:
import serial,time
ser=serial.Serial('/dev/serial0',9600,timeout=1)
AUTHORIZED_CARD="enter_your_card_no"
print("RFID Access System Ready")
print("Tap your card...")
try:
    while True:
        data=ser.read(12)
        if data:
            card_id=data.decode('utf-8').strip()
            print("Card Detected: "+card_id)
            if card_id==AUTHORIZED_CARD:
                print(" Access Granted — Hello!")
            else:
                print(" Access Denied — Nah!")
            time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    ser.close()
