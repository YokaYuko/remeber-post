#Tutti gli import necessari

from datetime import datetime
import telebot
from telebot import util, types
from telebot import types
from telebot.apihelper import send_animation, send_message, upload_sticker_file

#################################################
#Variabili principali

bot = telebot.TeleBot("5507623814:AAHoDyqHzoDE06_TtXd3Z7-10ejnqPuzO-s") #Istanza del bot

admins = {
    "Monday": "@YukoNakitsu",
    "Tuesday": "@Miliguer",
    "Wednesday": "@Spartacus16ssl",
    "Thursday": "@Silverio99",
    "Friday": "@RonXD",
    "Saturday": "@Demenziale482oro"
}

#################################################
#Funzioni

def t():
  return datetime.now()

#################################################
#Messaggi

in_group_reminder = "🔔 REMINDER 🔔\nHey {}, domani è il tuo turno!\nPreparati a postare :D"

#################################################

for day in days:
    if(dt(t().year,t().month,t().day+1).strftime("%A") == (day) and (t().hour==19)):
        bot.send_message(-1001492371018, in_group_reminder.replace("%who%", days[day])))
        print((t().day+1))

#################################################
#Eventi
        
@bot.message_handler()
def start_command(message):
    if message.chat.type != "private":
        return
    
    chat_id = message.chat.id

    bot.send_message(chat_id, "boh")

#################################################

bot.polling(none_stop=True)
