# callback.py

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import CallbackContext, ConversationHandler

from src.db import User
from src.config import Settings


def showMainMenu() -> None:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text='🔥 Mahsulotlar', web_app=WebAppInfo(url=Settings.wep_app)), KeyboardButton('📥Savat')
            ],
            [
                KeyboardButton('💼 Hamkorlik'), KeyboardButton("ℹ️ Ma'lumot")
            ],
            [
                KeyboardButton('🌐 Tilni tanlash')
            ]
        ],
        resize_keyboard=True
    )
    
    
def showLanguage(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Iltimos, tilni tanlang\nПожалуйста, выберите язык ⬇️',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='🇷🇺 Русский',
                        callback_data='language_ru'
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🇺🇿 O'zbekcha",
                        callback_data='language_uz'
                    )
                ]
            ]
        )
    )
    

def back() -> None:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("⬅️ Ortga")
            ]
        ],
        resize_keyboard=True
    )


def start(update: Update, context: CallbackContext) -> None:
    if update.message:
        messange = update.message.from_user
        user = User()
        if user.check_ds(messange.id, messange.full_name, messange.username):
            showLanguage(update, context)
        else:
            update.message.reply_text(
                text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!\n\nIjodimizga qiziqish bildirganingiz uchun tashakkur!\n\nHozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)\n\nToshkent bo‘yicha yetkazib berish: 1–3 ish kuni\nO‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuniO‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi\n\n450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!\n\nAgar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
                reply_markup=showMainMenu()
            )
    elif update.callback_query:
        query = update.callback_query
        query.answer()
        query.message.delete()
        query.message.reply_text(
            text=f"""Assalomu Alaykum, {query.from_user.first_name}!\n\nIjodimizga qiziqish bildirganingiz uchun tashakkur!\n\nHozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)\n\nToshkent bo‘yicha yetkazib berish: 1–3 ish kuni\nO‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuniO‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi\n\n450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!\n\nAgar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
            reply_markup=showMainMenu()
        )
    
        
def sendCart(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(text="<b>Sizning savatingiz bo'sh</b>")


def help(update: Update, context: CallbackContext) -> None:
    # update.message.reply_text(text='')
    pass


def sendCooperation(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.\n\nMenejer bilan bog'lanish uchun: @tirik_chilik")


def sendInformation(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="Kerakli bo'limni tanlang ⬇️",
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton("✍ Izoh qoldirish")
                ],
                [
                    KeyboardButton("🚀 Yetkazib berish shartlari"), KeyboardButton("☎ Kontaktlar")
                ],
                [
                    KeyboardButton("🏠 Bosh menyu")
                ]
            ]
        )
    )
    

def leaveComment(update: Update, context: CallbackContext) -> None:
    text = (
        "✅ Tirikchilik loyihasini tanlaganingiz uchun rahmat.\n"\
        "Bizning xizmatlarimiz sifatini yaxshilashga yordam bersangiz juda xursand bo’lar edik :)\n"\
        "Buning uchun 5 ballik tizim asosida bizni baholang yoki o'z tilaklaringizni yozib jo'nating."
    )
    if update.message.text =="🏠 Bosh menyu":
        start(update, context)
        return ConversationHandler.END
    
    update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton('😊 Menga hamma narsa yoqdi, 5 ❤️')
                ],
                [
                    KeyboardButton('🙂 Yaxshi, 4 ⭐⭐⭐⭐')
                ],
                [
                    KeyboardButton("😐 Qo'niqarli, 3 ⭐⭐⭐")
                ],
                [
                    KeyboardButton("😕 Yoqmadi, 2 ⭐⭐")
                ],
                [
                    KeyboardButton("😫 Men shikoyat qilmoqchiman 👎")
                ],
                [
                    KeyboardButton("🏠 Bosh menyu")
                ]
            ]
        )
    )
    return Settings.CHECKRATE
        

def checkRate(update: Update, context: CallbackContext) -> None:
    rate = [
        '😊 Menga hamma narsa yoqdi, 5 ❤️',
        '🙂 Yaxshi, 4 ⭐⭐⭐⭐', "😐 Qo'niqarli, 3 ⭐⭐⭐",
        "😕 Yoqmadi, 2 ⭐⭐","😫 Men shikoyat qilmoqchiman 👎"
    ]
    
    if update.message.text == "🏠 Bosh menyu":
        start(update, context)
        return ConversationHandler.END
    
    for r in rate:
        if update.message.text == r:
            update.message.reply_text(
                text='Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?',
                reply_markup=back()
            )
            return Settings.COMMENT
            

def sendComment(update: Update, context: CallbackContext) -> None:
    if update.message.text == "⬅️ Ortga":
        leaveComment(update, context)
        return Settings.RATE
    elif update.message.text == "🏠 Bosh menyu":
        pass
    else:
        text = 'Izoh uchun rahmat'
        if context.user_data.get('lang') == 'en':
            text = 'thank for your comment'
        update.message.reply_text(
            text=text,
            reply_markup=showMainMenu(),
        )
        return ConversationHandler.END


def sendDeliveryTerms(update: Update, context: CallbackContext) -> None:
    text = (
        "🚚 *Yetkazib berish shartlari:*\n\n"
        "• Toshkent bo‘yicha: 1–3 ish kuni — *30 000 so‘m*\n"
        "• O‘zbekiston bo‘yicha: 3–7 ish kuni — *40 000 so‘m*\n"
        "• Jo‘natmalar: *Seshanba* va *Juma* kunlari jo‘natiladi\n\n"
        "🟢 *450 000 so‘mdan ortiq buyurtmalar uchun yetkazib berish — bepul!*"
    )
    update.message.reply_text(text, parse_mode='Markdown')
    

def sendContacts(update: Update, context: CallbackContext) -> None:
    text = (
        "Teskari aloqa uchun:\n"\
        "@tirik_chilik"
    )
    update.message.reply_text(text)