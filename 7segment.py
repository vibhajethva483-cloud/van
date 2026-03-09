# Practical :
# Aim: Displaying Time over 4-Digit 7-Segment Display using Raspberry Pi.
#  Hardware Requirements
# Raspberry Pi 
# TM1637 4-Digit Seven Segment Display
# MicroSD card with Raspberry Pi OS installed
# Power supply for Raspberry Pi
# Jumper wires (male-to-female as needed)
# Monitor, keyboard, mouse (for setup)
# Software Requirements
# Raspberry Pi OS installed and running
# Python 3 
# RPi.GPIO library 



# Circuit Connections:

# TM1637 Board Pin--Physical PIN Number --GPIO Number 
# CLK--38--GPIO 20
# DIO--40--GPIO 21
# VCC--1--3.3 V
# GND--6--GROUND

#  Command to download the library:
# pip3 install raspberrypi-tm1637

# Source Code:
Clock Display:
from time import sleep
import tm1637  # Your modified library above

try:
    import thread
except ImportError:
    import _thread as thread

Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)  

try:
    print("Starting clock in the background (press CTRL + C to stop):")
    Display.StartClock(military_time=True)      
    sleep(1)
    Display.ShowDoublepoint(False)             
    sleep(5)
    Display.StopClock()                         
    
except KeyboardInterrupt:
    Display.cleanup()
