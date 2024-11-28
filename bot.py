import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Replace this with your bot's API token
API_TOKEN = "7605669588:AAHP6RNFa2M0R1fDSHAJY3oQnL-x4G3PXWU"
WEB_APP_URL = "https://developer-alif.github.io/mini-mining-app./"  # Replace with your Web App URL

bot = telebot.TeleBot(API_TOKEN)

# Start command
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    # Create a WebAppInfo object with your app URL
    web_app_info = WebAppInfo(url=WEB_APP_URL)
    # Inline keyboard with a Play button
    keyboard = InlineKeyboardMarkup()
    play_button = InlineKeyboardButton("🎮 Play", web_app=web_app_info)  # Use WebAppInfo here
    keyboard.add(play_button)
    bot.send_message(
        user_id,
        "Welcome to the Mini Mining Bot! Click the button below to start mining:",
        reply_markup=keyboard
    )

# Run the bot
bot.polling()
