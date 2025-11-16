#bot.py
import imghdr
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler

from src.config import Settings
from src.callbacks import start, help, sendCart, sendCooperation, sendInformation, sendDeliveryTerms, sendContacts, leaveComment, checkRate, sendComment, showLanguage



def main() -> None:
    updater = Updater(Settings.TOKEN)
    global dispatcher
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
    dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni tanlash"), showLanguage))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.text("✍ Izoh qoldirish"), leaveComment)],
        states={
            Settings.CHECKRATE:[
                MessageHandler(Filters.text & ~Filters.command, checkRate)
            ],
            Settings.COMMENT: [
                MessageHandler(Filters.text & ~Filters.command, sendComment)
            ],
            Settings.RATE: [
                MessageHandler(Filters.text & ~Filters.command, leaveComment)
            ] 
        },
        fallbacks={}
    ))
    dispatcher.add_handler(MessageHandler(Filters.text("🏠 Bosh menyu"), start))
    dispatcher.add_handler(MessageHandler(Filters.text("🚀 Yetkazib berish shartlari"), sendDeliveryTerms))
    dispatcher.add_handler(MessageHandler(Filters.text("☎ Kontaktlar"), sendContacts))
    
    updater.start_polling()
    updater.idle()
    
try:
    main()
except:
    dispatcher.add_handler(CommandHandler('Serverda xatolik qayta xabar yuboring'))
    dispatcher.add_handler(MessageHandler('Serverda xatolik qayta xabar yuboring'))