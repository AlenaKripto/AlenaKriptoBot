import os
import telegram
from flask import Flask, request

app = Flask(__name__)
bot = telegram.Bot(token=os.environ['BOT_TOKEN'])

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.lower()

    if '/start' in text:
        bot.send_message(chat_id=chat_id, text='Привет, Алена! Я готов к работе.')
    elif '/позови_меня' in text:
        bot.send_message(chat_id=chat_id, text='Эй! Проверь рынок!')
    elif '/прогноз' in text:
        bot.send_message(chat_id=chat_id, text='Прогноз: сегодня возможна волатильность на DOGE и SOL.')
    else:
        bot.send_message(chat_id=chat_id, text='Команда не распознана. Используй /start, /позови_меня или /прогноз.')

    return 'ok'
