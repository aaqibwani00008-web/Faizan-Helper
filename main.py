import os
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Hello Faizan!\n\n"
        "Main tumhara AI Assistant hoon.\n"
        "Kuch bhi poochho 😊"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = client.responses.create(
            model="gpt-5.6-mini",
            input=update.message.text
        )

        await update.message.reply_text(response.output_text)

    except Exception:
        await update.message.reply_text(
            "❌ Sorry, abhi kuch problem aa gayi."
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("🤖 AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
