import telebot
import threading
import time
import subprocess
import os

def working_message():
    i = 0
    while True:
        print("\rWorking" + "." * i, end="")
        i = (i + 1) % 4
        time.sleep(1)
# 啟動display_working_message執行緒
thread = threading.Thread(target=working_message)
thread.daemon = True
thread.start()

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "使用 /s 來獲得當前電腦的螢幕截圖。")

@bot.message_handler(commands=['s'])
def send_screenshot(message):
    screenshot_path = 'screenshot_temp.png'
    subprocess.run(['scrot', screenshot_path])
    with open(screenshot_path, 'rb') as file:
        bot.send_photo(message.chat.id, file)
    os.remove(screenshot_path)



bot.polling(none_stop=True)