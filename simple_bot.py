
from telegram import Bot, Update, ParseMode
from telegram.ext import CommandHandler, MessageHandler, Updater, ConversationHandler, Filters

import sqlite3
import model


bot_token = '5544320586:AAFaJ_z5clFBK6vVeUwpR0suqBeUOj84G8g'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений

# def show_all():
#     conn = sqlite3.connect('phonebook.db')
#     cursor = conn.cursor()
#     cursor.execute("select * from phonebook")
#     results = cursor.fetchall()
#     for i in results:
#         print(i)
#     return results


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Это телефонный справочник\n Выберите: \n Показать всех /show_all \n")

def show_all(update, context):
    context.bot.send_message(update.effective_chat.id, '{}'.format(model.show_all()))
    return 1

def convert_output(update, context):
    update.message.reply_text(f'{update.message.text} кг = {int(update.message.text) * 1000} гр')



def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



convert_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('show_all', show_all)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, convert_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )




start_handler = CommandHandler('start', start)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(convert_handler)

updater.start_polling()
updater.idle()