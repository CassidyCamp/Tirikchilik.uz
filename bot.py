from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from src.config import Settings
from src.callbacks import start, help, sendCart, sendCooperation, sendInformation

def main() -> None:
    updater = Updater(Settings.TOKEN)
    dispatcher = updater.dispatcher
    
    # Command Hendler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    
    # Query Hendler
    dispatcher.add_handler(CallbackQueryHandler(start, pattern='language_uz'))
    dispatcher.add_handler(CallbackQueryHandler(start, pattern='language_ru'))
    
    # Message Hendler
    dispatcher.add_handler(MessageHandler(Filters.text('📥Savat'), sendCart))
    dispatcher.add_handler(MessageHandler(Filters.text('💼 Hamkorlik'), sendCooperation))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Ma'lumot"), sendInformation))
    
    updater.start_polling()
    updater.idle()
    
main()