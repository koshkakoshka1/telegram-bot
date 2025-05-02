from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("7512431286:AAFAI_t1PjVqNJl4BfsjVaD_EXxJHlyRESQ")

def get_daily_analysis():
    matches = [
        "1️⃣ Црвена Звезда vs Будучность (ABA League) — Победа Звезды с форой -6.5",
        "2️⃣ Валенсия vs Бильбао (ACB) — Тотал меньше 164.5",
        "3️⃣ Реал Мадрид vs Манреса (ACB) — Фора -12.5 на Реал",
        "4️⃣ Лимож vs Бур (LNB Pro A) — ИТМ Бура 75.5",
        "5️⃣ УНИКС vs Нижний Новгород (VTB) — 1-я четверть: Тотал больше 38.5",
        "6️⃣ Партизан vs Мега Баскет (ABA) — Фора -9.5 на Партизан",
        "7️⃣ Фенербахче vs Дарюшшафака (Турция) — Тотал больше 166.5",
        "8️⃣ Олимпиакос vs Лаврио (Греция) — Фора -16.5 на Олимпиакос",
        "9️⃣ Альба vs Ульм (BBL Германия) — Тотал больше 171.5",
        "🔟 Монако vs Гравлин (Франция) — Фора -11.5 на Монако"
    ]
    return "*📊 Прогнозы на сегодня:*\n\n" + "\n".join(matches)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /top10 — и я пришлю тебе лучшие ставки дня 🏀")

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(get_daily_analysis())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))

print("Бот запущен...")
app.run_polling()
