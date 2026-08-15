import telebot
from google import genai

TELEGRAM_TOKEN = "8657969423:AAGYFZvVqIKvkVFCa_JIEkRrTC3tKONVgHI"
GEMINI_API_KEY = "AQ.Ab8RN6JgLLLwGIKSop39MEtFsiaaXF9iX29dbpK8mC_O48aTgg"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")

bot.infinity_polling()
