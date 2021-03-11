from telegram import *
from telegram.ext import *

key = "telegram bot key"

bot = Bot(key)
updater = Updater(key, use_context=True)
dispatcher = updater.dispatcher

def hi_function(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id = update.effective_chat.id,
		text = "hello",
		)

cmdHi = CommandHandler('hi',hi_function)
dispatcher.add_handler(cmdHi)
//exchange1

//exchange2


updater.start_polling()

