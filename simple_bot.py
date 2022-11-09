
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
    context.bot.send_message(update.effective_chat.id, f"Привет! Это телефонный справочник\n Выберите: \n Показать всех /show_all \n\
 Найти по фамилии /find_by_surname\n Добавить запись /add_record\n Удалить запись /delete_record")

def show_all(update, context):
    context.bot.send_message(update.effective_chat.id, '{}'.format(model.show_all()))

def find_by_surname(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите фамилию для поиска: ')
    return 1

def find_by_surname_output(update, context):
    update.message.reply_text('{}'.format(model.find_by_surname(update.message.text)), ParseMode.MARKDOWN)
    



def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



show_all_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('show_all', show_all)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_by_surname_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

find_by_surname_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('find_by_surname', find_by_surname)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_by_surname_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )




start_handler = CommandHandler('start', start)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_all_handler)
dispatcher.add_handler(find_by_surname_handler)

updater.start_polling()
updater.idle()