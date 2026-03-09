# Aim: Capturing image and video with PiCamera and Raspberry Pi.
#  Hardware Requirements
# Raspberry Pi 
# Picamera
# MicroSD card with Raspberry Pi OS installed
# Power supply for Raspberry Pi
# Monitor, keyboard, mouse (for setup)
# Software Requirements
# Raspberry Pi OS installed and running
# Python 3 
# Circuit Connections:
# Direct connection on the board through the Camera channel. 
# Commands:
# sudo raspi-config  - # for configuring interface I2C
# Interface -> enable Camera
# reboot
# sudo apt-get update
# sudo apt-get upgrade
# sudo apt install python3-picamera
# Source Code For Image:
from picamera import PiCamera
import datetime,os

os.makedirs('/home/pi/images',exist_ok=True)
camera=PiCamera()
camera.resolution=(1024,768)
camera.capture("{}/image_{}.jpg".format('/home/pi/images',datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
# Source Code For Video:
from picamera import PiCamera
from time import sleep
import datetime,os,subprocess

os.makedirs('/home/pi/videos',exist_ok=True)
camera=PiCamera();camera.resolution=(1024,768)
ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
video_h264="/home/pi/videos/video_{}.h264".format(ts)
camera.start_recording(video_h264);sleep(10);camera.stop_recording()
subprocess.run(["MP4Box","-add",video_h264,"/home/pi/videos/video_{}.mp4".format(ts)],check=True);os.remove(video_h264)
