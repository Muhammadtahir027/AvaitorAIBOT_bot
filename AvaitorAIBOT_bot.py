from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN = "8195936639:AAFHzXO70k_MoBJTz2Wz6GgSb8QymmfR-hI"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["Play Prediction"]]
    await update.message.reply_text(
        "Bot is running! How can I help you?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    )

# Prediction logic
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prediction = round(random.uniform(2.0, 500.0), 2)
    await update.message.reply_text(
        f"Prediction: {prediction}x\n(صرف اندازہ ہے، اصلی Aviator data سے connect نہیں ہے)"
    )

# Main bot setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex("^(Play Prediction)$"), play))

print("Bot is running...")
app.run_polling()