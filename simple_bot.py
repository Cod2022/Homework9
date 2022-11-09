from random import randint

from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Updater, ConversationHandler, Filters
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


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Это телефонный справичник\n Выберите: \n Показать всех /convert \n")

def convert(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите количество килограммов, \n или нажмите /stop для выхода из бота ")
    return 1

def convert_output(update, context):
    update.message.reply_text(f'{update.message.text} кг = {int(update.message.text) * 1000} гр')



def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



convert_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('convert', convert)],
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