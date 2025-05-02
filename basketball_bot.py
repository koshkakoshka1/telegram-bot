from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

def get_daily_analysis():
    return (
        "🏀 *Матч дня: Бург vs Ле-Портель (3 мая 2025)*\n\n"
        "*Форма:*\n"
        "- Бург: 4 поражения подряд, но играет дома\n"
        "- Ле-Портель: 7 поражений в 8 матчах\n\n"
        "*Ставки:*\n"
        "- Победа Бурга с форой -9.5\n"
        "- Live: победа Бурга во 2-й четверти\n"
        "- Бетбилдер: победа Бурга + тотал > 160.5\n\n"
        "_Прогнозируемый счёт: 88–72_"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /today — и я пришлю матч дня.")

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(get_daily_analysis())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("today", today))

print("Бот запущен...")
app.run_polling()
