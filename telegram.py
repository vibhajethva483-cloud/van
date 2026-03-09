# Practical :
# Aim: Controlling Raspberry Pi with Telegram App.
#  Hardware Requirements
# Raspberry Pi 
# MicroSD card with Raspberry Pi OS installed
# Power supply for Raspberry Pi
# Jumper wires (male-to-female as needed)
# Monitor, keyboard, mouse (for setup)

# Software Requirements
# Raspberry Pi OS installed and running
# Python 3 
# RPi.GPIO library 
# Circuit Connections:

#  Board Pin - Physical PIN Number - GPIO Number 
# GPIO - 40 -GPIO 21
# GND -6 -GROUND


# Step to get bot on Telegram app:
# 1:  Download Telegram on your mobile phone.
# 2: Install Telegram.
# 2:   Open Telegram app in your system or mobile
# 3: Click On Start Messaging Button
# 4: Enter your mobile number to register with the telegram service.
# 5: Search for name "BotFather"
# 6: Click on "BotFather
# 7: To Start "BotFather" type /start in message
# 8: Now type /newbot in message  . and then give the name to your BOT and Username also.

#  Commands to download the library:
# sudo apt-get install python-pip
# sudo pip install telepot


Source Code:
import time
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

LED_PIN = 40  # Pin 40 = GPIO21
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, 0)
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command:', command)

    if 'On' in command or 'on' in command:
        GPIO.output(LED_PIN, 1)
        bot.sendMessage(chat_id, "LED turned ON")
    elif 'Off' in command or 'off' in command:
        GPIO.output(LED_PIN, 0)
        bot.sendMessage(chat_id, "LED turned OFF")
    else:
        bot.sendMessage(chat_id, "Send 'on' or 'off' to control the LED.")

# Insert your bot token here
bot = telepot.Bot('BOT_TOKEN')
MessageLoop(bot, action).run_as_thread()
print('Listening for commands...')
while True:
    time.sleep(10)