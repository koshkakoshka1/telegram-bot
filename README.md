# Telegram Basketball Bot

Простой Telegram-бот для отправки прогноза на баскетбольный матч дня.

## Запуск

1. Установи зависимости:
```
pip install -r requirements.txt
```

2. Экспортируй переменную TOKEN:
```
export TOKEN=your_telegram_bot_token
```

3. Запусти бота:
```
python basketball_bot.py
```

## Деплой на Render

- Залей файлы в GitHub
- Создай Web Service на https://render.com
- В Start Command укажи:
```
python basketball_bot.py
```
