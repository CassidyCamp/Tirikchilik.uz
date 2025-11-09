from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import CallbackContext

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
    

def start(update: Update, context: CallbackContext) -> None:
    if update.message:
        messange = update.message.from_user
        user = User()
        if user.check_ds(messange.id, messange.full_name, messange.username):
            showLanguage(update, context)
        else:
            update.message.reply_text(text='salom')
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
                    KeyboardButton("Izoh qoldirish")
                ],
                [
                    KeyboardButton("Yetkazib berish shartlari")
                ],
                [
                    KeyboardButton("Kontaktlar")
                ]
            ]
        )
    )