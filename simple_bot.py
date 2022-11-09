from random import randint

from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Updater, ConversationHandler, Filters

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
    context.bot.send_message(update.effective_chat.id, f"Привет! Это конвертер\калькулятор!\n Выберите: \n Конвертация кг в гр /convert \n Калькулятор /calc")

def convert(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите количество килограммов, \n или нажмите /stop для выхода из бота ")
    return 1

def convert_output(update, context):
    update.message.reply_text(f'{update.message.text} кг = {int(update.message.text) * 1000} гр')

def calc(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите выражение для калькуляции, \n или нажмите /stop для выхода из бота ")
    return 1

def calc_output(update, context):
    update.message.reply_text(eval(update.message.text))





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

calc_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('calc', calc)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, calc_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )




start_handler = CommandHandler('start', start)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(convert_handler)
dispatcher.add_handler(calc_handler)

updater.start_polling()
updater.idle()