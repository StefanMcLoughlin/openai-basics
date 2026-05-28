from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

openai_client = OpenAI()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hallo, der AI Bot funktioniert.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai_client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Du bist ein hilfreicher AI Assistent.
        Antworte kurz, freundlich und verständlich.

        User Nachricht:
        {user_message}
        """
    )

    await update.message.reply_text(response.output_text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot läuft...")
    app.run_polling()

if __name__ == "__main__":
    main()
