import telebot
import pyautogui
import os

pathDestop = r'C:\Users\golik\OneDrive\Рабочий стол\\'

API_TOKEN = '5458248024:AAEudqi2NGN9YWekYKHfTVUEgf4RwqkV68g'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I\'m Iris.")

@bot.message_handler(commands=['screen', 'screenshot'])
def screen(message):
    scr = pyautogui.screenshot().save(r'D:\\codes\\IrisBotTelegram\\lastScreenshot\scr.png')
    
    photo = open('D:\codes\IrisBotTelegram\\lastScreenshot\scr.png', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['shutdown'])
def shutdown(message):
    os.system('shutdown -s')

@bot.message_handler(commands=['open'])
def open(message):
    os.startfile(pathDestop + 'lol.txt')


bot.infinity_polling()