import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace this with your bot's API token
API_TOKEN = "7605669588:AAHP6RNFa2M0R1fDSHAJY3oQnL-x4G3PXWU"
WEB_APP_URL = "https://developer-alif.github.io/mini-mining-app./"  # Replace with your Web App URL

bot = telebot.TeleBot(API_TOKEN)

# Start command
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    # Inline keyboard with a Play button
    keyboard = InlineKeyboardMarkup()
    play_button = InlineKeyboardButton(
        "ðŸŽ® Play", web_app=WEB_APP_URL  # Opens the mini mining app
    )
    keyboard.add(play_button)
    bot.send_message(
        user_id,
        "Welcome to the Mini Mining Bot! Click the button below to start mining:",
        reply_markup=keyboard
    )

# Run the bot
bot.polling()
