
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import uvicorn

# Получаем токен и URL из переменных окружения
TOKEN = os.environ.get("TOKEN")
BOT_URL = os.environ.get("BOT_URL")

# Создаём Telegram приложение
telegram_app = ApplicationBuilder().token(TOKEN).build()

# Команды бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /top10 — и я пришлю тебе лучшие ставки дня 🏀")

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown("*📊 Прогнозы появятся здесь каждый день*")

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("top10", top10))

# Инициализируем FastAPI-приложение
fastapi_app = FastAPI()

# Установка вебхука при старте
@fastapi_app.on_event("startup")
async def on_startup():
    await telegram_app.bot.delete_webhook()
    await telegram_app.bot.set_webhook(f"{BOT_URL}/webhook")

# Обработка входящих обновлений от Telegram
@fastapi_app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}

# Запуск FastAPI-сервера
if __name__ == "__main__":
    uvicorn.run("basketball_bot:fastapi_app", host="0.0.0.0", port=10000)
