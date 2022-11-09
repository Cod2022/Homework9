# Телеграм-бот телефонный справочник

from telegram import Bot, Update, ParseMode
from telegram.ext import CommandHandler, MessageHandler, Updater, ConversationHandler, Filters

import sqlite3
import model


bot_token = '5544320586:AAFaJ_z5clFBK6vVeUwpR0suqBeUOj84G8g'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Это телефонный справочник\n Выберите: \n Показать всех /show \n\
 Найти по фамилии /find \n Добавить запись /add \n Удалить запись /delete")

def show_all(update, context):
    context.bot.send_message(update.effective_chat.id, '{}'.format(model.show_all()))

def find_by_surname(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите фамилию для поиска: ')
    return 1

def find_by_surname_output(update, context):
    update.message.reply_text('{}'.format(model.find_by_surname(update.message.text)), ParseMode.MARKDOWN)
    
def add_record(update, context):
    context.bot.send_message(update.effective_chat.id, 'Через пробел введите номер записи(id), фамилию, имя, отчество, номер телефона: ')
    return 1

def add_record_output(update, context):
    update.message.reply_text(f'Добавлена запись: {update.message.text}', model.add_record(update.message.text))

def delete_record(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите номер записи, которую вы хотите удалить: ')
    return 1

def delete_record_output(update, context):
    update.message.reply_text(f'Запись {update.message.text} удалена', model.delete_record(update.message.text))



def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



show_all_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('show', show_all)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_by_surname_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

find_by_surname_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('find', find_by_surname)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_by_surname_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

add_record_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('add', add_record)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, add_record_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

delete_record_handler = ConversationHandler(
        
        
        entry_points=[CommandHandler('delete', delete_record)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, delete_record_output)],
            
        },
        fallbacks=[CommandHandler('stop', stop)]
    )




start_handler = CommandHandler('start', start)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_all_handler)
dispatcher.add_handler(find_by_surname_handler)
dispatcher.add_handler(add_record_handler)
dispatcher.add_handler(delete_record_handler)

updater.start_polling()
updater.idle()