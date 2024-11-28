import telebot

API_TOKEN = "7605669588:AAHP6RNFa2M0R1fDSHAJY3oQnL-x4G3PXWU"
bot = telebot.TeleBot(API_TOKEN)

# Start command
@bot.message_handler(commands=["start"])
def start(message):
    # Send the Web App link
    bot.send_message(
        message.chat.id,
        "Welcome to the Coin Mining Game! Tap below to start mining.",
        reply_markup=telebot.types.ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True
        ).add(
            telebot.types.KeyboardButton(
                "Play",
                web_app=telebot.types.WebAppInfo(url="https://developer-alif.github.io/mini-mining-app./")  # Link to your hosted mini app
            )
        )
    )

bot.polling()
