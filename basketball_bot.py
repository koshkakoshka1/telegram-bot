from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

def get_daily_analysis():
    matches = [
        "1️⃣ Бург vs Ле-Портель — Победа Бурга с форой -9.5",
        "2️⃣ Зенит vs ЦСКА — Тотал меньше 162.5",
        "3️⃣ Реал vs Барселона — Победа Реала",
        "4️⃣ Локомотив vs УНИКС — 1-я четверть > 39.5",
        "5️⃣ Панатинаикос vs Олимпиакос — ИТБ2 84.5",
        "6️⃣ Брешия vs Виртус — Победа Виртуса",
        "7️⃣ Галатасарай vs Эфес — Победа Эфеса с форой -4",
        "8️⃣ Анадолу vs Дарюшшафака — Тотал больше 168.5",
        "9️⃣ Партизан vs Црвена Звезда — Фора -2 на хозяев",
        "🔟 Монако vs Валенсия — Монако и тотал больше 161.5"
    ]
    return "*📊 Прогнозы на сегодня:*

" + "\n".join(matches)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /top10 — и я пришлю тебе лучшие ставки дня 🏀")

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(get_daily_analysis())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))

print("Бот запущен...")
app.run_polling()
