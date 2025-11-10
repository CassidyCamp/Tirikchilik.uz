# Tirikchilik.uz - Telegram Bot

Tirikchilik.uz telegram boti - bu foydalanuvchilarga turli xizmatlarni taqdim etuvchi automatlashtirilgan telegram bot.

## 🚀 Bot Vazifalari

- 📱 Foydalanuvchilarga asosiy menyular taqdim etish
- 💼 Hamkorlik imkoniyatlarini ko'rsatish
- 🛒 Savat xizmati
- ℹ️ Ma'lumot berish xizmati
- 🚀 Yetkazib berish shartlari
- ☎️ Kontaktlar
- ✍️ Izoh qoldirish imkoniyati
- 🌐 Tilni tanlash (O'zbek/Rus)

## 📋 Talablar

- Python 3.10+
- python-telegram-bot==13.15
- python-dotenv==1.2.1
- APScheduler==3.6.3
- Boshqa talablar `requirements.txt` faylida ko'rsatilgan

## 🔧 O'rnatish

1. **Repository klonlash:**
```bash
git clone https://github.com/sizning-repo-url.git
cd tirikchilik.uz
```

2. **Virtual muhit yaratish:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows
```

3. **Talab qilinadigan paketlarni o'rnatish:**
```bash
pip install -r requirements.txt
```

4. **Muhit o'zgaruvchilarini sozlash:**
```bash
cp src/.env.example src/.env
```

`src/.env` fayliga quyidagi o'zgaruvchilarni kiriting:
```
TOKEN=your_telegram_bot_token_here
DataUser=database/datauser.json
DataUserpPhone=database/datauserphone.json
wep_app=your_web_app_url
```

## 🚦 Ishga Tushirish

### Mahalliy (Local) Ishga Tushirish

```bash
python bot.py
```

### Railway Platformasiga Joylash

1. **Railway hisobiga ega bo'lish:**
   - [Railway](https://railway.com/) saytiga boring
   - Hisob oching yoki kiring

2. **GitHub bilan ulash:**
   - Repositoryingizni GitHub ga joylang
   - Railway hisobingizda "New Project" tugmasini bosing
   - "Deploy from GitHub Repo" tanlang
   - Repositoryingizni tanlang

3. **Muhit o'zgaruvchilarini sozlash (Railway):**
   - Railway dashboardda sizning loyihangizga o'ting
   - "Variables" bo'limiga o'ting
   - Quyidagi o'zgaruvchilarni qo'shing:
     ```
     TOKEN=your_telegram_bot_token_here
     DataUser=database/datauser.json
     DataUserpPhone=database/datauserphone.json
     wep_app=your_web_app_url
     ```

4. **Avtomatik deploy:**
   - Railway avtomatik tarzda sizning kodingizni build qiladi va deploy qiladi
   - Deploy jarayonini "Deploy" bo'limida kuzatishingiz mumkin

## 📁 Loyiha Tuzilishi

```
tirikchilik.uz/
├── bot.py                 # Asosiy bot fayli
├── requirements.txt       # Python paketlari
├── Procfile              # Railway uchun process fayli
├── README.md             # Ushbu fayl
├── database/             # Ma'lumotlar bazasi fayllari
│   ├── datauser.json
│   └── datauserphone.json
└── src/                  # Bot modullari
    ├── .env              # Muhit o'zgaruvchilari
    ├── .env.example      # Muhit o'zgaruvchilari namunasi
    ├── config.py         # Konfiguratsiya fayli
    ├── callbacks.py      # Bot callback funksiyalari
    └── db.py            # Ma'lumotlar bazasi funksiyalari
```

## 🔧 Konfiguratsiya

### Telegram Bot Token Olish

1. [BotFather](https://t.me/botfather) botiga o'ting
2. `/newbot` komandasini yuboring
3. Bot nomini kiriting
4. Bot username kiriting (oxirida `bot` bo'lishi kerak)
5. Token nusxalab oling

### Railway Sozlamalari

- **Procfile:** Railway platformasi uchun process fayli
- **Buildpack:** Python buildpack avtomatik tarzda o'rnatiladi
- **Port:** Railway avtomatik tarzda port ajratadi

## 🐛 Xatolarni Tuzatish

### Umumiy Xatolar

1. **Token xatosi:**
   - Token to'g'riligini tekshiring
   - `.env` faylida token borligini tekshiring

2. **Database xatosi:**
   - `database/` papka mavjudligini tekshiring
   - Fayl ruxsatlarini tekshiring

3. **Deploy xatosi:**
   - Loglarni tekshiring (Railway dashboard)
   - Muhit o'zgaruvchilarini tekshiring

## 📞 Qo'llab-quvvatlash

Agar muammo yuzaga kelsa:
1. Railway loglarini tekshiring
2. GitHub Issues yaratib, muammoni tavsiflang
3. Telegram: @sizning_username

## 📄 Litsenziya

Ushbu loyiha MIT litsenziyasi ostida tarqatiladi.

## 🎯 Funktsiyalar

- ✅ Asosiy menyular
- ✅ Hamkorlik bo'limi
- ✅ Savat xizmati
- ✅ Ma'lumot bo'limi
- ✅ Yetkazib berish shartlari
- ✅ Kontaktlar
- ✅ Izoh qoldirish
- ✅ Tilni tanlash
- ✅ Railway platformasiga tayyor

## 🔗 Foydali Havolalar

- [Railway Dokumentatsiyasi](https://docs.railway.app/)
- [Python Telegram Bot Dokumentatsiyasi](https://python-telegram-bot.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

**Tirikchilik.uz** - Sizning ishonchli telegram botingiz! 🤖