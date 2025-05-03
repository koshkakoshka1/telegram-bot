
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import uvicorn

TOKEN = os.environ.get("TOKEN")
BOT_URL = os.environ.get("BOT_URL")

telegram_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /top10 — и я пришлю тебе лучшие ставки дня 🏀")

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown("*📊 Прогнозы появятся здесь каждый день*")

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("top10", top10))

fastapi_app = FastAPI()

@fastapi_app.on_event("startup")
async def on_startup():
    await telegram_app.initialize()
    print("🚀 Telegram bot initialized")
    await telegram_app.bot.delete_webhook()
    await telegram_app.bot.set_webhook(f"{BOT_URL}/webhook")
    print(f"✅ Webhook set to {BOT_URL}/webhook")

@fastapi_app.post("/webhook")
async def handle_webhook(request: Request):
    print("📩 Webhook hit!")
    try:
        data = await request.json()
        print("✅ JSON получен")
        update = Update.de_json(data, telegram_app.bot)
        print("🔄 Update распарсен")
        await telegram_app.process_update(update)
        print("🎉 Обновление обработано")
        return {"ok": True}
    except Exception as e:
        print("❌ Webhook error:", e)
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("basketball_bot:fastapi_app", host="0.0.0.0", port=8080)
