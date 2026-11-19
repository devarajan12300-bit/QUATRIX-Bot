import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to QUATRIX Bot! 🚀\nBot is working successfully."
    )

def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("QUATRIX Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
