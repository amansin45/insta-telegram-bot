from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# Bot token Render ke environment se uthaya jaayega
TOKEN = os.getenv("7203036903:AAGx5Pbbdh4jHigEA_cN2ch1iHLA_I0msCA")

# Start command ke liye function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send me your Instagram username to get tips.")

# Har normal message ke liye function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips = (
        "📈 Instagram Growth Tips:\n"
        "1. Post Reels daily\n"
        "2. Use trending hashtags\n"
        "3. Engage with your audience\n"
        "4. Run giveaways\n"
        "5. Collaborate with others\n"
